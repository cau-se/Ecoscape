import os
import pathlib
import traceback

import kubernetes
import yaml
from kubernetes import config

class K8sClient:
    def __init__(self):
        config.load_incluster_config()

        self.client = kubernetes.dynamic.DynamicClient(
            kubernetes.client.api_client.ApiClient()
        )
        c = self.client.configuration.get_default_copy()
        c.verify_ssl = False
        self.client.configuration.set_default(c)

    def apply_item(self, manifest: dict, verbose: bool = False, is_delete = False):
        api_version = manifest.get("apiVersion")
        kind = manifest.get("kind")
        resource_name = manifest.get("metadata").get("name")
        namespace = manifest.get("metadata").get("namespace")
        crd_api = self.client.resources.get(api_version=api_version, kind=kind)

        if is_delete:
            crd_api.delete(namespace=namespace, name=resource_name)
        else:
            try:
                crd_api.get(namespace=namespace, name=resource_name)
                crd_api.patch(body=manifest, content_type="application/merge-patch+json")
                if verbose:
                    print(f"{namespace}/{resource_name} patched")
            except kubernetes.dynamic.exceptions.NotFoundError:
                crd_api.create(body=manifest, namespace=namespace)
                if verbose:
                    print(f"{namespace}/{resource_name} created")

    def apply_yaml(self,
                   filepath: pathlib.Path,
                   verbose: bool = False,
                   is_delete = False):
        with open(filepath, 'r') as f:
            manifest = yaml.safe_load(f)
            self.apply_item(manifest=manifest, verbose=verbose, is_delete=is_delete)

    def apply_directory(
            self,
            directory,
            is_delete
    ):
        try:
            filenames = os.listdir(directory)
            for filename in filenames:
                full_path = os.path.join(directory, filename)  # get the full path.
                if os.path.isfile(full_path): # check if it is a file.
                    try:
                        self.apply_yaml(full_path, is_delete=is_delete)  # pass the full path to the process_file function.
                    except Exception as e:
                        traceback.print_exc()
        except FileNotFoundError:
            print(f"Directory not found: {directory}")

    def create_directory(self, directory):
        self.apply_directory(directory, False)

    def delete_directory(self, directory):
        self.apply_directory(directory, True)