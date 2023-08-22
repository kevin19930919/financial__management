import subprocess

# ----- util functions -----
def run_container(container, image_repo, image_tag):
    pop = subprocess.Popen(
        f'docker run --rm -id --name {container} {image_repo}:{image_tag}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = pop.communicate()
    stderr = stderr.decode('utf-8')
    stdout = stdout.decode("utf-8")
    if stderr:
        print(f"fail to start container {stderr}")
        return False
    return True


class DockerContainer():
    def __init__(self, container=None):
        self.container = container
    
    def copy_file_in_container(self, target_path, file_path):
        if self.container:
            pop = subprocess.Popen(
                f'docker cp {file_path} {self.container}:{target_path}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = pop.communicate()
            stderr = stderr.decode('utf-8')
            stdout = stdout.decode("utf-8")
            if stderr:
                print(f"fail to cp file container {stderr}")
                return False
            return True

    def exec_command_in_container(self, command):
        if self.container:
            pop = subprocess.Popen(
                f'docker exec {self.container} /bin/sh -c "{command}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = pop.communicate()
            stderr = stderr.decode('utf-8')
            stdout = stdout.decode("utf-8")
            print(stdout)


    def stop_container(self):
        if self.container:
            pop = subprocess.Popen(
                f'docker stop {self.container}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = pop.communicate()
            stderr = stderr.decode('utf-8')
            stdout = stdout.decode("utf-8")
            if stderr:
                print(f"fail to stop container {stderr}")
                return False
            return True

