from cloudengine import CloudProvider


class ACCloud:
    def __init__(self, provider: CloudProvider, bucket_name: str):
        self.provider = provider
        self.bucket_name = bucket_name

    def find_files(self, query: str, max_result: int) -> list[str]:
        response = self.provider.filter_by_query(
            bucket=self.bucket_name, query=query, max=max_result
        )

        return response["result"]["data"]


class VideoStorage:
    def __init__(self, provider: CloudProvider) -> None:
        self.bucket_name = "video-backup.arjancodes.com"
        self.region = "eu-west-1c"
        self.access_cloud = ACCloud(provider=provider, bucket_name=self.bucket_name)
