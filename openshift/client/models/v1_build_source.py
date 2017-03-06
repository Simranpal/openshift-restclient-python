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


class V1BuildSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, binary=None, context_dir=None, dockerfile=None, git=None, images=None, secrets=None, source_secret=None, type=None):
        """
        V1BuildSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'binary': 'V1BinaryBuildSource',
            'context_dir': 'str',
            'dockerfile': 'str',
            'git': 'V1GitBuildSource',
            'images': 'list[V1ImageSource]',
            'secrets': 'list[V1SecretBuildSource]',
            'source_secret': 'V1LocalObjectReference',
            'type': 'str'
        }

        self.attribute_map = {
            'binary': 'binary',
            'context_dir': 'contextDir',
            'dockerfile': 'dockerfile',
            'git': 'git',
            'images': 'images',
            'secrets': 'secrets',
            'source_secret': 'sourceSecret',
            'type': 'type'
        }

        self._binary = binary
        self._context_dir = context_dir
        self._dockerfile = dockerfile
        self._git = git
        self._images = images
        self._secrets = secrets
        self._source_secret = source_secret
        self._type = type

    @property
    def binary(self):
        """
        Gets the binary of this V1BuildSource.
        binary builds accept a binary as their input. The binary is generally assumed to be a tar, gzipped tar, or zip file depending on the strategy. For Docker builds, this is the build context and an optional Dockerfile may be specified to override any Dockerfile in the build context. For Source builds, this is assumed to be an archive as described above. For Source and Docker builds, if binary.asFile is set the build will receive a directory with a single file. contextDir may be used when an archive is provided. Custom builds will receive this binary as input on STDIN.

        :return: The binary of this V1BuildSource.
        :rtype: V1BinaryBuildSource
        """
        return self._binary

    @binary.setter
    def binary(self, binary):
        """
        Sets the binary of this V1BuildSource.
        binary builds accept a binary as their input. The binary is generally assumed to be a tar, gzipped tar, or zip file depending on the strategy. For Docker builds, this is the build context and an optional Dockerfile may be specified to override any Dockerfile in the build context. For Source builds, this is assumed to be an archive as described above. For Source and Docker builds, if binary.asFile is set the build will receive a directory with a single file. contextDir may be used when an archive is provided. Custom builds will receive this binary as input on STDIN.

        :param binary: The binary of this V1BuildSource.
        :type: V1BinaryBuildSource
        """

        self._binary = binary

    @property
    def context_dir(self):
        """
        Gets the context_dir of this V1BuildSource.
        contextDir specifies the sub-directory where the source code for the application exists. This allows to have buildable sources in directory other than root of repository.

        :return: The context_dir of this V1BuildSource.
        :rtype: str
        """
        return self._context_dir

    @context_dir.setter
    def context_dir(self, context_dir):
        """
        Sets the context_dir of this V1BuildSource.
        contextDir specifies the sub-directory where the source code for the application exists. This allows to have buildable sources in directory other than root of repository.

        :param context_dir: The context_dir of this V1BuildSource.
        :type: str
        """

        self._context_dir = context_dir

    @property
    def dockerfile(self):
        """
        Gets the dockerfile of this V1BuildSource.
        dockerfile is the raw contents of a Dockerfile which should be built. When this option is specified, the FROM may be modified based on your strategy base image and additional ENV stanzas from your strategy environment will be added after the FROM, but before the rest of your Dockerfile stanzas. The Dockerfile source type may be used with other options like git - in those cases the Git repo will have any innate Dockerfile replaced in the context dir.

        :return: The dockerfile of this V1BuildSource.
        :rtype: str
        """
        return self._dockerfile

    @dockerfile.setter
    def dockerfile(self, dockerfile):
        """
        Sets the dockerfile of this V1BuildSource.
        dockerfile is the raw contents of a Dockerfile which should be built. When this option is specified, the FROM may be modified based on your strategy base image and additional ENV stanzas from your strategy environment will be added after the FROM, but before the rest of your Dockerfile stanzas. The Dockerfile source type may be used with other options like git - in those cases the Git repo will have any innate Dockerfile replaced in the context dir.

        :param dockerfile: The dockerfile of this V1BuildSource.
        :type: str
        """

        self._dockerfile = dockerfile

    @property
    def git(self):
        """
        Gets the git of this V1BuildSource.
        git contains optional information about git build source

        :return: The git of this V1BuildSource.
        :rtype: V1GitBuildSource
        """
        return self._git

    @git.setter
    def git(self, git):
        """
        Sets the git of this V1BuildSource.
        git contains optional information about git build source

        :param git: The git of this V1BuildSource.
        :type: V1GitBuildSource
        """

        self._git = git

    @property
    def images(self):
        """
        Gets the images of this V1BuildSource.
        images describes a set of images to be used to provide source for the build

        :return: The images of this V1BuildSource.
        :rtype: list[V1ImageSource]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this V1BuildSource.
        images describes a set of images to be used to provide source for the build

        :param images: The images of this V1BuildSource.
        :type: list[V1ImageSource]
        """

        self._images = images

    @property
    def secrets(self):
        """
        Gets the secrets of this V1BuildSource.
        secrets represents a list of secrets and their destinations that will be used only for the build.

        :return: The secrets of this V1BuildSource.
        :rtype: list[V1SecretBuildSource]
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """
        Sets the secrets of this V1BuildSource.
        secrets represents a list of secrets and their destinations that will be used only for the build.

        :param secrets: The secrets of this V1BuildSource.
        :type: list[V1SecretBuildSource]
        """

        self._secrets = secrets

    @property
    def source_secret(self):
        """
        Gets the source_secret of this V1BuildSource.
        sourceSecret is the name of a Secret that would be used for setting up the authentication for cloning private repository. The secret contains valid credentials for remote repository, where the data's key represent the authentication method to be used and value is the base64 encoded credentials. Supported auth methods are: ssh-privatekey.

        :return: The source_secret of this V1BuildSource.
        :rtype: V1LocalObjectReference
        """
        return self._source_secret

    @source_secret.setter
    def source_secret(self, source_secret):
        """
        Sets the source_secret of this V1BuildSource.
        sourceSecret is the name of a Secret that would be used for setting up the authentication for cloning private repository. The secret contains valid credentials for remote repository, where the data's key represent the authentication method to be used and value is the base64 encoded credentials. Supported auth methods are: ssh-privatekey.

        :param source_secret: The source_secret of this V1BuildSource.
        :type: V1LocalObjectReference
        """

        self._source_secret = source_secret

    @property
    def type(self):
        """
        Gets the type of this V1BuildSource.
        type of build input to accept

        :return: The type of this V1BuildSource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1BuildSource.
        type of build input to accept

        :param type: The type of this V1BuildSource.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

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
        if not isinstance(other, V1BuildSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
