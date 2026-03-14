+++
title = "AWS S3 Bucket"
weight = 80
+++

Amazon Simple Storage Service (Amazon S3) 是一种对象存储服务，提供静态网站托管。我们将看看通过 GitHub Actions 构建 Zola 网站并将其部署到 S3 所需的设置。

## AWS 设置

[AWS 官方开发者指南](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started-cloudfront-overview.html) 详细说明了如何创建存储桶并正确设置它以进行静态网站托管。在 AWS 中，你不仅可以托管网站文件，还可以购买域名并通过他们的全球 CDN (CloudFront) 加速你的网站。

为了让 GitHub Actions 修改存储桶中的文件，你需要在你的 AWS 帐户中创建一个 IAM 用户，该用户具有刚好足够的权限来执行我们需要执行的操作，而不会更多。

首先，我们需要创建一个新策略，方法是登录 AWS 控制台并转到 **IAM** > **Policies** > **Create policy**。从可视化编辑器切换到 **JSON** 并粘贴以下代码段。请记住更新你的存储桶名称：

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AccessToWebsiteBuckets",
      "Effect": "Allow",
      "Action": [
        "s3:PutBucketWebsite",
        "s3:PutObject",
        "s3:PutObjectAcl",
        "s3:GetObject",
        "s3:ListBucket",
        "s3:DeleteObject"
      ],
      "Resource": [
        "arn:aws:s3:::Bucket-Name"
        "arn:aws:s3:::Bucket-Name/*"
      ]
    },
    {
      "Sid": "AccessToCloudfront",
      "Effect": "Allow",
      "Action": ["cloudfront:GetInvalidation", "cloudfront:CreateInvalidation"],
      "Resource": "*"
    }
  ]
}
```

如果你不打算使用 CloudFront 加速你的网站，则不需要 `AccessToCloudfront` 部分。

创建策略后，你需要在 **IAM** > **Users** 下创建一个新用户。给它一个名字，例如 `github-actions-user`。在 **Set permissions** 步骤中，选择 **Attach policies directly** 并找到我们在上一步中创建的策略。

从用户列表中点击你新创建的帐户，然后打开 **Security Credentials** 选项卡。在 **Access keys** 下选择 > **Create access key** 并选择 **Command Line Interface (CLI)**。点击 "I understand the above recommendation"，然后点击 **Create access key**。记下 **Access key ID** 和 **Secret access key**。

## 在 GitHub 中设置 Secrets

我们刚刚创建的访问密钥需要在你的 GitHub 仓库中配置为 secret。为此，导航到 **Setting** > 展开 **Secrets and variables** > 点击 **Actions**。

在 **Repository secrets** 下点击 **Add repository secret**。在 *Name* 字段中输入 `AWS_ACCESS_KEY_ID`，在 *Secret* 字段中输入上一步中的值。对 secret access key 执行相同的操作，将其命名为 `AWS_SECRET_ACCESS_KEY`。最后，为你的存储桶名称创建一个名为 `S3_BUCKET` 的 secret，如果你为你的网站创建了分发，则创建一个 `CLOUDFRONT_DISTRIBUTION_ID`。

## GitHub Actions

接下来我们需要创建 *Github Action* 来构建并将我们的文件部署到 S3。我们需要在仓库的 `.github/workflows` 目录下创建一个工作流文件。这可以通过在 GitHub 中导航到 *Actions* 选项卡或从你的机器提交文件来完成。

`.github/workflows/publish.yml`:

```yaml
name: Build and Publish to AWS
on:
  push:
    branches:
      - main
jobs:
  run:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v3
      - uses: taiki-e/install-action@v2
        with:
          tool: zola@0.17.2
      - name: Build
        run: zola build
      - uses: reggionick/s3-deploy@v4
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        with:
          folder: public
          bucket: ${{ secrets.S3_BUCKET }}
          private: true
          bucket-region: us-east-1
          # 仅当你创建了 CloudFront 分发时才使用以下两项
          dist-id: ${{ secrets.CLOUDFRONT_DISTRIBUTION_ID }}
          invalidation: /*
```

注意，如果你希望有不同的行为，你可能需要在上面的代码段中更改分支名称。
