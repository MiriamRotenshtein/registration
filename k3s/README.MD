# K3S

## What is it?

K3s is a fully conformant production-ready Kubernetes distribution with the following changes:

- It is packaged as a single binary.
- It adds support for sqlite3 as the default storage backend. Etcd3, MySQL, and Postgres are also supported.
- It wraps Kubernetes and other components in a single, simple launcher.
- It is secure by default with reasonable defaults for lightweight environments.
- It has minimal to no OS dependencies *(just a sane kernel and cgroup mounts needed)*.
- It eliminates the need to expose a port on Kubernetes worker nodes for the kubelet API by exposing this API to the Kubernetes control plane nodes over a websocket tunnel.

## Why should I use it?

- Production ready and secure.
- Easy to install.
- Half the memory. 
- All in a binary less than 100 MB.
- Certified Kubernetes distribution designed for production workloads  in unattended,
remote locations or inside IoT *("Internet of Things" - Devices that are connected and can communicate with other devices)* appliances.

## When should it be used?

In addition to where the above benefits are important to me.
Kubernetes, or K8s, is an open-source, portable, and scalable container orchestration platform. 
With K8s, you can reliably manage distributed systems for your applications, enabling declarative configuration and automatic deployment.

## Where can it be used?

K3s is a lightweight and fast Kubernetes file system, 
and is designed for use in remedial environments and limited resources,
and is effective for solving light operations or smaller business needs.

