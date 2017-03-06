# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'unversioned.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: v1.5.0-alpha3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1NodeSystemInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, architecture=None, boot_id=None, container_runtime_version=None, kernel_version=None, kube_proxy_version=None, kubelet_version=None, machine_id=None, operating_system=None, os_image=None, system_uuid=None):
        """
        V1NodeSystemInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'architecture': 'str',
            'boot_id': 'str',
            'container_runtime_version': 'str',
            'kernel_version': 'str',
            'kube_proxy_version': 'str',
            'kubelet_version': 'str',
            'machine_id': 'str',
            'operating_system': 'str',
            'os_image': 'str',
            'system_uuid': 'str'
        }

        self.attribute_map = {
            'architecture': 'architecture',
            'boot_id': 'bootID',
            'container_runtime_version': 'containerRuntimeVersion',
            'kernel_version': 'kernelVersion',
            'kube_proxy_version': 'kubeProxyVersion',
            'kubelet_version': 'kubeletVersion',
            'machine_id': 'machineID',
            'operating_system': 'operatingSystem',
            'os_image': 'osImage',
            'system_uuid': 'systemUUID'
        }

        self._architecture = architecture
        self._boot_id = boot_id
        self._container_runtime_version = container_runtime_version
        self._kernel_version = kernel_version
        self._kube_proxy_version = kube_proxy_version
        self._kubelet_version = kubelet_version
        self._machine_id = machine_id
        self._operating_system = operating_system
        self._os_image = os_image
        self._system_uuid = system_uuid

    @property
    def architecture(self):
        """
        Gets the architecture of this V1NodeSystemInfo.
        The Architecture reported by the node

        :return: The architecture of this V1NodeSystemInfo.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this V1NodeSystemInfo.
        The Architecture reported by the node

        :param architecture: The architecture of this V1NodeSystemInfo.
        :type: str
        """
        if architecture is None:
            raise ValueError("Invalid value for `architecture`, must not be `None`")

        self._architecture = architecture

    @property
    def boot_id(self):
        """
        Gets the boot_id of this V1NodeSystemInfo.
        Boot ID reported by the node.

        :return: The boot_id of this V1NodeSystemInfo.
        :rtype: str
        """
        return self._boot_id

    @boot_id.setter
    def boot_id(self, boot_id):
        """
        Sets the boot_id of this V1NodeSystemInfo.
        Boot ID reported by the node.

        :param boot_id: The boot_id of this V1NodeSystemInfo.
        :type: str
        """
        if boot_id is None:
            raise ValueError("Invalid value for `boot_id`, must not be `None`")

        self._boot_id = boot_id

    @property
    def container_runtime_version(self):
        """
        Gets the container_runtime_version of this V1NodeSystemInfo.
        ContainerRuntime Version reported by the node through runtime remote API (e.g. docker://1.5.0).

        :return: The container_runtime_version of this V1NodeSystemInfo.
        :rtype: str
        """
        return self._container_runtime_version

    @container_runtime_version.setter
    def container_runtime_version(self, container_runtime_version):
        """
        Sets the container_runtime_version of this V1NodeSystemInfo.
        ContainerRuntime Version reported by the node through runtime remote API (e.g. docker://1.5.0).

        :param container_runtime_version: The container_runtime_version of this V1NodeSystemInfo.
        :type: str
        """
        if container_runtime_version is None:
            raise ValueError("Invalid value for `container_runtime_version`, must not be `None`")

        self._container_runtime_version = container_runtime_version

    @property
    def kernel_version(self):
        """
        Gets the kernel_version of this V1NodeSystemInfo.
        Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).

        :return: The kernel_version of this V1NodeSystemInfo.
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        """
        Sets the kernel_version of this V1NodeSystemInfo.
        Kernel Version reported by the node from 'uname -r' (e.g. 3.16.0-0.bpo.4-amd64).

        :param kernel_version: The kernel_version of this V1NodeSystemInfo.
        :type: str
        """
        if kernel_version is None:
            raise ValueError("Invalid value for `kernel_version`, must not be `None`")

        self._kernel_version = kernel_version

    @property
    def kube_proxy_version(self):
        """
        Gets the kube_proxy_version of this V1NodeSystemInfo.
        KubeProxy Version reported by the node.

        :return: The kube_proxy_version of this V1NodeSystemInfo.
        :rtype: str
        """
        return self._kube_proxy_version

    @kube_proxy_version.setter
    def kube_proxy_version(self, kube_proxy_version):
        """
        Sets the kube_proxy_version of this V1NodeSystemInfo.
        KubeProxy Version reported by the node.

        :param kube_proxy_version: The kube_proxy_version of this V1NodeSystemInfo.
        :type: str
        """
        if kube_proxy_version is None:
            raise ValueError("Invalid value for `kube_proxy_version`, must not be `None`")

        self._kube_proxy_version = kube_proxy_version

    @property
    def kubelet_version(self):
        """
        Gets the kubelet_version of this V1NodeSystemInfo.
        Kubelet Version reported by the node.

        :return: The kubelet_version of this V1NodeSystemInfo.
        :rtype: str
        """
        return self._kubelet_version

    @kubelet_version.setter
    def kubelet_version(self, kubelet_version):
        """
        Sets the kubelet_version of this V1NodeSystemInfo.
        Kubelet Version reported by the node.

        :param kubelet_version: The kubelet_version of this V1NodeSystemInfo.
        :type: str
        """
        if kubelet_version is None:
            raise ValueError("Invalid value for `kubelet_version`, must not be `None`")

        self._kubelet_version = kubelet_version

    @property
    def machine_id(self):
        """
        Gets the machine_id of this V1NodeSystemInfo.
        MachineID reported by the node. For unique machine identification in the cluster this field is prefered. Learn more from man(5) machine-id: http://man7.org/linux/man-pages/man5/machine-id.5.html

        :return: The machine_id of this V1NodeSystemInfo.
        :rtype: str
        """
        return self._machine_id

    @machine_id.setter
    def machine_id(self, machine_id):
        """
        Sets the machine_id of this V1NodeSystemInfo.
        MachineID reported by the node. For unique machine identification in the cluster this field is prefered. Learn more from man(5) machine-id: http://man7.org/linux/man-pages/man5/machine-id.5.html

        :param machine_id: The machine_id of this V1NodeSystemInfo.
        :type: str
        """
        if machine_id is None:
            raise ValueError("Invalid value for `machine_id`, must not be `None`")

        self._machine_id = machine_id

    @property
    def operating_system(self):
        """
        Gets the operating_system of this V1NodeSystemInfo.
        The Operating System reported by the node

        :return: The operating_system of this V1NodeSystemInfo.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """
        Sets the operating_system of this V1NodeSystemInfo.
        The Operating System reported by the node

        :param operating_system: The operating_system of this V1NodeSystemInfo.
        :type: str
        """
        if operating_system is None:
            raise ValueError("Invalid value for `operating_system`, must not be `None`")

        self._operating_system = operating_system

    @property
    def os_image(self):
        """
        Gets the os_image of this V1NodeSystemInfo.
        OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).

        :return: The os_image of this V1NodeSystemInfo.
        :rtype: str
        """
        return self._os_image

    @os_image.setter
    def os_image(self, os_image):
        """
        Sets the os_image of this V1NodeSystemInfo.
        OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)).

        :param os_image: The os_image of this V1NodeSystemInfo.
        :type: str
        """
        if os_image is None:
            raise ValueError("Invalid value for `os_image`, must not be `None`")

        self._os_image = os_image

    @property
    def system_uuid(self):
        """
        Gets the system_uuid of this V1NodeSystemInfo.
        SystemUUID reported by the node. For unique machine identification MachineID is prefered. This field is specific to Red Hat hosts https://access.redhat.com/documentation/en-US/Red_Hat_Subscription_Management/1/html/RHSM/getting-system-uuid.html

        :return: The system_uuid of this V1NodeSystemInfo.
        :rtype: str
        """
        return self._system_uuid

    @system_uuid.setter
    def system_uuid(self, system_uuid):
        """
        Sets the system_uuid of this V1NodeSystemInfo.
        SystemUUID reported by the node. For unique machine identification MachineID is prefered. This field is specific to Red Hat hosts https://access.redhat.com/documentation/en-US/Red_Hat_Subscription_Management/1/html/RHSM/getting-system-uuid.html

        :param system_uuid: The system_uuid of this V1NodeSystemInfo.
        :type: str
        """
        if system_uuid is None:
            raise ValueError("Invalid value for `system_uuid`, must not be `None`")

        self._system_uuid = system_uuid

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1NodeSystemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
