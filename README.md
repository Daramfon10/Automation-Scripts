# Setting up Azure Machines to run MLPERF Inference Benchmark
## Overview
This repository contains a script that helps with setting up the software dependencies on the machine to successfully run the benchmark. The following should be achieved when the script is ran:
1. Update docker to the latest version
2. Raid the NVME disks to get extra space to store the images,data,preprocessed data and models. Once the disks are raided successfully, it will be mounted on the machine.
3. Update the docker root directory path to a location(**/mnt/resource_nvme/docker**) in the mounted NVME disk so there will be enough space for images to be stored.
4. Check that NVIDIA driver version has been updated and if not point user in the right direction to make update. 
5. Add user to docker group to avoid docker permissions issue.

## Prerequisites
1. Spin up a VM with the **Ubuntu-HPC(18.04/20.04)** image 
2. After deployment is complete, connect to the machine

## How to run the script
1. Clone the repository on your VM - `git clone `
2. Change directory to the cloned repository - `cd MLPerf-SystemSetup/`
3. Run the script by running the command `bash config.sh <MLPERF_recommended_driver_version>`

## Verification
1. To make sure the docker has been updated to the recommended version, run - `docker --version`
2. Check if the /dev/md128 disk has been mounted on the /mnt/resource_nvme - `df -h | grep "/mnt/resource_nvme"`
3. Check if the docker root directory has been updated to **/mnt/resource_nvme/docker** - `docker info | grep "Docker Root Dir"`. 
4. Run - `nvidia-smi | grep "Driver"`. Check to make sure the driver matches the recommended driver version. In the case that it does not match, click on the link -[NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) to update the driver to the recommended version.
5. For docker permissions issue, run - `docker info`. To verify success, this command should run successfully without any permissions error.
