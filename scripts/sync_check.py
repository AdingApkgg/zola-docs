#!/usr/bin/env python3
import os
import urllib.request
import urllib.error
import hashlib
import sys
import ssl

# Configuration
LOCAL_CONTENT_DIR = "content/documentation"
UPSTREAM_BASE_URL = "https://raw.githubusercontent.com/getzola/zola/master/docs/content/documentation"

def get_remote_content(url):
    try:
        context = ssl._create_unverified_context()
        with urllib.request.urlopen(url, context=context) as response:
            return response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print(f"Error fetching {url}: {e.code} {e.reason}")
        return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def calculate_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def normalize_content(content):
    # Normalize line endings and trailing whitespace for comparison
    lines = content.strip().splitlines()
    return "\n".join([line.rstrip() for line in lines])

def main():
    print(f"Checking synchronization with upstream: {UPSTREAM_BASE_URL}")
    print(f"Scanning local directory: {LOCAL_CONTENT_DIR}")
    print("-" * 60)

    differences = []
    missing_upstream = []
    checked_count = 0

    for root, dirs, files in os.walk(LOCAL_CONTENT_DIR):
        for file in files:
            if file.endswith(".en.md"):
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, LOCAL_CONTENT_DIR)
                
                # Construct upstream path
                # Remove .en.md and replace with .md
                upstream_relative_path = relative_path[:-6] + ".md"
                upstream_url = f"{UPSTREAM_BASE_URL}/{upstream_relative_path}"
                
                # Special handling for _index.en.md -> _index.md
                if file == "_index.en.md":
                     upstream_relative_path = relative_path[:-6] + ".md"
                     upstream_url = f"{UPSTREAM_BASE_URL}/{upstream_relative_path}"

                print(f"Checking: {relative_path} -> {upstream_relative_path} ...", end=" ", flush=True)

                # Read local content
                try:
                    with open(local_path, 'r', encoding='utf-8') as f:
                        local_content = f.read()
                except Exception as e:
                    print(f"Failed to read local file: {e}")
                    continue

                # Fetch remote content
                remote_content = get_remote_content(upstream_url)
                
                if remote_content is None:
                    missing_upstream.append(local_path)
                    print("MISSING UPSTREAM")
                    continue

                checked_count += 1

                # Compare
                if normalize_content(local_content) != normalize_content(remote_content):
                    print("DIFFERENT")
                    differences.append((local_path, upstream_url))
                else:
                    print("OK")

    print("-" * 60)
    print(f"Checked {checked_count} files.")
    
    if missing_upstream:
        print(f"\nFiles not found in upstream ({len(missing_upstream)}):")
        for path in missing_upstream:
            print(f"  - {path}")

    if differences or missing_upstream:
        if differences:
            print(f"\nFiles with differences ({len(differences)}):")
            for local, remote in differences:
                print(f"  - {local}")
                print(f"    Upstream: {remote}")
        
        if missing_upstream:
             # Already printed above, just ensure exit code is non-zero
             pass

        sys.exit(1)
    else:
        print("\nAll files are in sync!")
        sys.exit(0)

if __name__ == "__main__":
    main()
