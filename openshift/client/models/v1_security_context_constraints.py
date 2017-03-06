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


class V1SecurityContextConstraints(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, allow_host_dir_volume_plugin=None, allow_host_ipc=None, allow_host_network=None, allow_host_pid=None, allow_host_ports=None, allow_privileged_container=None, allowed_capabilities=None, api_version=None, default_add_capabilities=None, fs_group=None, groups=None, kind=None, metadata=None, priority=None, read_only_root_filesystem=None, required_drop_capabilities=None, run_as_user=None, se_linux_context=None, seccomp_profiles=None, supplemental_groups=None, users=None, volumes=None):
        """
        V1SecurityContextConstraints - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'allow_host_dir_volume_plugin': 'bool',
            'allow_host_ipc': 'bool',
            'allow_host_network': 'bool',
            'allow_host_pid': 'bool',
            'allow_host_ports': 'bool',
            'allow_privileged_container': 'bool',
            'allowed_capabilities': 'list[str]',
            'api_version': 'str',
            'default_add_capabilities': 'list[str]',
            'fs_group': 'V1FSGroupStrategyOptions',
            'groups': 'list[str]',
            'kind': 'str',
            'metadata': 'V1ObjectMeta',
            'priority': 'int',
            'read_only_root_filesystem': 'bool',
            'required_drop_capabilities': 'list[str]',
            'run_as_user': 'V1RunAsUserStrategyOptions',
            'se_linux_context': 'V1SELinuxContextStrategyOptions',
            'seccomp_profiles': 'list[str]',
            'supplemental_groups': 'V1SupplementalGroupsStrategyOptions',
            'users': 'list[str]',
            'volumes': 'list[str]'
        }

        self.attribute_map = {
            'allow_host_dir_volume_plugin': 'allowHostDirVolumePlugin',
            'allow_host_ipc': 'allowHostIPC',
            'allow_host_network': 'allowHostNetwork',
            'allow_host_pid': 'allowHostPID',
            'allow_host_ports': 'allowHostPorts',
            'allow_privileged_container': 'allowPrivilegedContainer',
            'allowed_capabilities': 'allowedCapabilities',
            'api_version': 'apiVersion',
            'default_add_capabilities': 'defaultAddCapabilities',
            'fs_group': 'fsGroup',
            'groups': 'groups',
            'kind': 'kind',
            'metadata': 'metadata',
            'priority': 'priority',
            'read_only_root_filesystem': 'readOnlyRootFilesystem',
            'required_drop_capabilities': 'requiredDropCapabilities',
            'run_as_user': 'runAsUser',
            'se_linux_context': 'seLinuxContext',
            'seccomp_profiles': 'seccompProfiles',
            'supplemental_groups': 'supplementalGroups',
            'users': 'users',
            'volumes': 'volumes'
        }

        self._allow_host_dir_volume_plugin = allow_host_dir_volume_plugin
        self._allow_host_ipc = allow_host_ipc
        self._allow_host_network = allow_host_network
        self._allow_host_pid = allow_host_pid
        self._allow_host_ports = allow_host_ports
        self._allow_privileged_container = allow_privileged_container
        self._allowed_capabilities = allowed_capabilities
        self._api_version = api_version
        self._default_add_capabilities = default_add_capabilities
        self._fs_group = fs_group
        self._groups = groups
        self._kind = kind
        self._metadata = metadata
        self._priority = priority
        self._read_only_root_filesystem = read_only_root_filesystem
        self._required_drop_capabilities = required_drop_capabilities
        self._run_as_user = run_as_user
        self._se_linux_context = se_linux_context
        self._seccomp_profiles = seccomp_profiles
        self._supplemental_groups = supplemental_groups
        self._users = users
        self._volumes = volumes

    @property
    def allow_host_dir_volume_plugin(self):
        """
        Gets the allow_host_dir_volume_plugin of this V1SecurityContextConstraints.
        AllowHostDirVolumePlugin determines if the policy allow containers to use the HostDir volume plugin

        :return: The allow_host_dir_volume_plugin of this V1SecurityContextConstraints.
        :rtype: bool
        """
        return self._allow_host_dir_volume_plugin

    @allow_host_dir_volume_plugin.setter
    def allow_host_dir_volume_plugin(self, allow_host_dir_volume_plugin):
        """
        Sets the allow_host_dir_volume_plugin of this V1SecurityContextConstraints.
        AllowHostDirVolumePlugin determines if the policy allow containers to use the HostDir volume plugin

        :param allow_host_dir_volume_plugin: The allow_host_dir_volume_plugin of this V1SecurityContextConstraints.
        :type: bool
        """
        if allow_host_dir_volume_plugin is None:
            raise ValueError("Invalid value for `allow_host_dir_volume_plugin`, must not be `None`")

        self._allow_host_dir_volume_plugin = allow_host_dir_volume_plugin

    @property
    def allow_host_ipc(self):
        """
        Gets the allow_host_ipc of this V1SecurityContextConstraints.
        AllowHostIPC determines if the policy allows host ipc in the containers.

        :return: The allow_host_ipc of this V1SecurityContextConstraints.
        :rtype: bool
        """
        return self._allow_host_ipc

    @allow_host_ipc.setter
    def allow_host_ipc(self, allow_host_ipc):
        """
        Sets the allow_host_ipc of this V1SecurityContextConstraints.
        AllowHostIPC determines if the policy allows host ipc in the containers.

        :param allow_host_ipc: The allow_host_ipc of this V1SecurityContextConstraints.
        :type: bool
        """
        if allow_host_ipc is None:
            raise ValueError("Invalid value for `allow_host_ipc`, must not be `None`")

        self._allow_host_ipc = allow_host_ipc

    @property
    def allow_host_network(self):
        """
        Gets the allow_host_network of this V1SecurityContextConstraints.
        AllowHostNetwork determines if the policy allows the use of HostNetwork in the pod spec.

        :return: The allow_host_network of this V1SecurityContextConstraints.
        :rtype: bool
        """
        return self._allow_host_network

    @allow_host_network.setter
    def allow_host_network(self, allow_host_network):
        """
        Sets the allow_host_network of this V1SecurityContextConstraints.
        AllowHostNetwork determines if the policy allows the use of HostNetwork in the pod spec.

        :param allow_host_network: The allow_host_network of this V1SecurityContextConstraints.
        :type: bool
        """
        if allow_host_network is None:
            raise ValueError("Invalid value for `allow_host_network`, must not be `None`")

        self._allow_host_network = allow_host_network

    @property
    def allow_host_pid(self):
        """
        Gets the allow_host_pid of this V1SecurityContextConstraints.
        AllowHostPID determines if the policy allows host pid in the containers.

        :return: The allow_host_pid of this V1SecurityContextConstraints.
        :rtype: bool
        """
        return self._allow_host_pid

    @allow_host_pid.setter
    def allow_host_pid(self, allow_host_pid):
        """
        Sets the allow_host_pid of this V1SecurityContextConstraints.
        AllowHostPID determines if the policy allows host pid in the containers.

        :param allow_host_pid: The allow_host_pid of this V1SecurityContextConstraints.
        :type: bool
        """
        if allow_host_pid is None:
            raise ValueError("Invalid value for `allow_host_pid`, must not be `None`")

        self._allow_host_pid = allow_host_pid

    @property
    def allow_host_ports(self):
        """
        Gets the allow_host_ports of this V1SecurityContextConstraints.
        AllowHostPorts determines if the policy allows host ports in the containers.

        :return: The allow_host_ports of this V1SecurityContextConstraints.
        :rtype: bool
        """
        return self._allow_host_ports

    @allow_host_ports.setter
    def allow_host_ports(self, allow_host_ports):
        """
        Sets the allow_host_ports of this V1SecurityContextConstraints.
        AllowHostPorts determines if the policy allows host ports in the containers.

        :param allow_host_ports: The allow_host_ports of this V1SecurityContextConstraints.
        :type: bool
        """
        if allow_host_ports is None:
            raise ValueError("Invalid value for `allow_host_ports`, must not be `None`")

        self._allow_host_ports = allow_host_ports

    @property
    def allow_privileged_container(self):
        """
        Gets the allow_privileged_container of this V1SecurityContextConstraints.
        AllowPrivilegedContainer determines if a container can request to be run as privileged.

        :return: The allow_privileged_container of this V1SecurityContextConstraints.
        :rtype: bool
        """
        return self._allow_privileged_container

    @allow_privileged_container.setter
    def allow_privileged_container(self, allow_privileged_container):
        """
        Sets the allow_privileged_container of this V1SecurityContextConstraints.
        AllowPrivilegedContainer determines if a container can request to be run as privileged.

        :param allow_privileged_container: The allow_privileged_container of this V1SecurityContextConstraints.
        :type: bool
        """
        if allow_privileged_container is None:
            raise ValueError("Invalid value for `allow_privileged_container`, must not be `None`")

        self._allow_privileged_container = allow_privileged_container

    @property
    def allowed_capabilities(self):
        """
        Gets the allowed_capabilities of this V1SecurityContextConstraints.
        AllowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field maybe added at the pod author's discretion. You must not list a capability in both AllowedCapabilities and RequiredDropCapabilities.

        :return: The allowed_capabilities of this V1SecurityContextConstraints.
        :rtype: list[str]
        """
        return self._allowed_capabilities

    @allowed_capabilities.setter
    def allowed_capabilities(self, allowed_capabilities):
        """
        Sets the allowed_capabilities of this V1SecurityContextConstraints.
        AllowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field maybe added at the pod author's discretion. You must not list a capability in both AllowedCapabilities and RequiredDropCapabilities.

        :param allowed_capabilities: The allowed_capabilities of this V1SecurityContextConstraints.
        :type: list[str]
        """
        if allowed_capabilities is None:
            raise ValueError("Invalid value for `allowed_capabilities`, must not be `None`")

        self._allowed_capabilities = allowed_capabilities

    @property
    def api_version(self):
        """
        Gets the api_version of this V1SecurityContextConstraints.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1SecurityContextConstraints.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1SecurityContextConstraints.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1SecurityContextConstraints.
        :type: str
        """

        self._api_version = api_version

    @property
    def default_add_capabilities(self):
        """
        Gets the default_add_capabilities of this V1SecurityContextConstraints.
        DefaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capabiility in both DefaultAddCapabilities and RequiredDropCapabilities.

        :return: The default_add_capabilities of this V1SecurityContextConstraints.
        :rtype: list[str]
        """
        return self._default_add_capabilities

    @default_add_capabilities.setter
    def default_add_capabilities(self, default_add_capabilities):
        """
        Sets the default_add_capabilities of this V1SecurityContextConstraints.
        DefaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capabiility in both DefaultAddCapabilities and RequiredDropCapabilities.

        :param default_add_capabilities: The default_add_capabilities of this V1SecurityContextConstraints.
        :type: list[str]
        """
        if default_add_capabilities is None:
            raise ValueError("Invalid value for `default_add_capabilities`, must not be `None`")

        self._default_add_capabilities = default_add_capabilities

    @property
    def fs_group(self):
        """
        Gets the fs_group of this V1SecurityContextConstraints.
        FSGroup is the strategy that will dictate what fs group is used by the SecurityContext.

        :return: The fs_group of this V1SecurityContextConstraints.
        :rtype: V1FSGroupStrategyOptions
        """
        return self._fs_group

    @fs_group.setter
    def fs_group(self, fs_group):
        """
        Sets the fs_group of this V1SecurityContextConstraints.
        FSGroup is the strategy that will dictate what fs group is used by the SecurityContext.

        :param fs_group: The fs_group of this V1SecurityContextConstraints.
        :type: V1FSGroupStrategyOptions
        """

        self._fs_group = fs_group

    @property
    def groups(self):
        """
        Gets the groups of this V1SecurityContextConstraints.
        The groups that have permission to use this security context constraints

        :return: The groups of this V1SecurityContextConstraints.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this V1SecurityContextConstraints.
        The groups that have permission to use this security context constraints

        :param groups: The groups of this V1SecurityContextConstraints.
        :type: list[str]
        """

        self._groups = groups

    @property
    def kind(self):
        """
        Gets the kind of this V1SecurityContextConstraints.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1SecurityContextConstraints.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1SecurityContextConstraints.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1SecurityContextConstraints.
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """
        Gets the metadata of this V1SecurityContextConstraints.
        Standard object's metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :return: The metadata of this V1SecurityContextConstraints.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1SecurityContextConstraints.
        Standard object's metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :param metadata: The metadata of this V1SecurityContextConstraints.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def priority(self):
        """
        Gets the priority of this V1SecurityContextConstraints.
        Priority influences the sort order of SCCs when evaluating which SCCs to try first for a given pod request based on access in the Users and Groups fields.  The higher the int, the higher priority.  If scores for multiple SCCs are equal they will be sorted by name.

        :return: The priority of this V1SecurityContextConstraints.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this V1SecurityContextConstraints.
        Priority influences the sort order of SCCs when evaluating which SCCs to try first for a given pod request based on access in the Users and Groups fields.  The higher the int, the higher priority.  If scores for multiple SCCs are equal they will be sorted by name.

        :param priority: The priority of this V1SecurityContextConstraints.
        :type: int
        """
        if priority is None:
            raise ValueError("Invalid value for `priority`, must not be `None`")

        self._priority = priority

    @property
    def read_only_root_filesystem(self):
        """
        Gets the read_only_root_filesystem of this V1SecurityContextConstraints.
        ReadOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the SCC should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.

        :return: The read_only_root_filesystem of this V1SecurityContextConstraints.
        :rtype: bool
        """
        return self._read_only_root_filesystem

    @read_only_root_filesystem.setter
    def read_only_root_filesystem(self, read_only_root_filesystem):
        """
        Sets the read_only_root_filesystem of this V1SecurityContextConstraints.
        ReadOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the SCC should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.

        :param read_only_root_filesystem: The read_only_root_filesystem of this V1SecurityContextConstraints.
        :type: bool
        """
        if read_only_root_filesystem is None:
            raise ValueError("Invalid value for `read_only_root_filesystem`, must not be `None`")

        self._read_only_root_filesystem = read_only_root_filesystem

    @property
    def required_drop_capabilities(self):
        """
        Gets the required_drop_capabilities of this V1SecurityContextConstraints.
        RequiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added.

        :return: The required_drop_capabilities of this V1SecurityContextConstraints.
        :rtype: list[str]
        """
        return self._required_drop_capabilities

    @required_drop_capabilities.setter
    def required_drop_capabilities(self, required_drop_capabilities):
        """
        Sets the required_drop_capabilities of this V1SecurityContextConstraints.
        RequiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added.

        :param required_drop_capabilities: The required_drop_capabilities of this V1SecurityContextConstraints.
        :type: list[str]
        """
        if required_drop_capabilities is None:
            raise ValueError("Invalid value for `required_drop_capabilities`, must not be `None`")

        self._required_drop_capabilities = required_drop_capabilities

    @property
    def run_as_user(self):
        """
        Gets the run_as_user of this V1SecurityContextConstraints.
        RunAsUser is the strategy that will dictate what RunAsUser is used in the SecurityContext.

        :return: The run_as_user of this V1SecurityContextConstraints.
        :rtype: V1RunAsUserStrategyOptions
        """
        return self._run_as_user

    @run_as_user.setter
    def run_as_user(self, run_as_user):
        """
        Sets the run_as_user of this V1SecurityContextConstraints.
        RunAsUser is the strategy that will dictate what RunAsUser is used in the SecurityContext.

        :param run_as_user: The run_as_user of this V1SecurityContextConstraints.
        :type: V1RunAsUserStrategyOptions
        """

        self._run_as_user = run_as_user

    @property
    def se_linux_context(self):
        """
        Gets the se_linux_context of this V1SecurityContextConstraints.
        SELinuxContext is the strategy that will dictate what labels will be set in the SecurityContext.

        :return: The se_linux_context of this V1SecurityContextConstraints.
        :rtype: V1SELinuxContextStrategyOptions
        """
        return self._se_linux_context

    @se_linux_context.setter
    def se_linux_context(self, se_linux_context):
        """
        Sets the se_linux_context of this V1SecurityContextConstraints.
        SELinuxContext is the strategy that will dictate what labels will be set in the SecurityContext.

        :param se_linux_context: The se_linux_context of this V1SecurityContextConstraints.
        :type: V1SELinuxContextStrategyOptions
        """

        self._se_linux_context = se_linux_context

    @property
    def seccomp_profiles(self):
        """
        Gets the seccomp_profiles of this V1SecurityContextConstraints.
        SeccompProfiles lists the allowed profiles that may be set for the pod or container's seccomp annotations.  An unset (nil) or empty value means that no profiles may be specifid by the pod or container. The wildcard '*' may be used to allow all profiles.  When used to generate a value for a pod the first non-wildcard profile will be used as the default.

        :return: The seccomp_profiles of this V1SecurityContextConstraints.
        :rtype: list[str]
        """
        return self._seccomp_profiles

    @seccomp_profiles.setter
    def seccomp_profiles(self, seccomp_profiles):
        """
        Sets the seccomp_profiles of this V1SecurityContextConstraints.
        SeccompProfiles lists the allowed profiles that may be set for the pod or container's seccomp annotations.  An unset (nil) or empty value means that no profiles may be specifid by the pod or container. The wildcard '*' may be used to allow all profiles.  When used to generate a value for a pod the first non-wildcard profile will be used as the default.

        :param seccomp_profiles: The seccomp_profiles of this V1SecurityContextConstraints.
        :type: list[str]
        """

        self._seccomp_profiles = seccomp_profiles

    @property
    def supplemental_groups(self):
        """
        Gets the supplemental_groups of this V1SecurityContextConstraints.
        SupplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext.

        :return: The supplemental_groups of this V1SecurityContextConstraints.
        :rtype: V1SupplementalGroupsStrategyOptions
        """
        return self._supplemental_groups

    @supplemental_groups.setter
    def supplemental_groups(self, supplemental_groups):
        """
        Sets the supplemental_groups of this V1SecurityContextConstraints.
        SupplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext.

        :param supplemental_groups: The supplemental_groups of this V1SecurityContextConstraints.
        :type: V1SupplementalGroupsStrategyOptions
        """

        self._supplemental_groups = supplemental_groups

    @property
    def users(self):
        """
        Gets the users of this V1SecurityContextConstraints.
        The users who have permissions to use this security context constraints

        :return: The users of this V1SecurityContextConstraints.
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """
        Sets the users of this V1SecurityContextConstraints.
        The users who have permissions to use this security context constraints

        :param users: The users of this V1SecurityContextConstraints.
        :type: list[str]
        """

        self._users = users

    @property
    def volumes(self):
        """
        Gets the volumes of this V1SecurityContextConstraints.
        Volumes is a white list of allowed volume plugins.  FSType corresponds directly with the field names of a VolumeSource (azureFile, configMap, emptyDir).  To allow all volumes you may use '*'.

        :return: The volumes of this V1SecurityContextConstraints.
        :rtype: list[str]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """
        Sets the volumes of this V1SecurityContextConstraints.
        Volumes is a white list of allowed volume plugins.  FSType corresponds directly with the field names of a VolumeSource (azureFile, configMap, emptyDir).  To allow all volumes you may use '*'.

        :param volumes: The volumes of this V1SecurityContextConstraints.
        :type: list[str]
        """
        if volumes is None:
            raise ValueError("Invalid value for `volumes`, must not be `None`")

        self._volumes = volumes

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
        if not isinstance(other, V1SecurityContextConstraints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
