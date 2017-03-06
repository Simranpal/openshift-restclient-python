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


class V1ImageSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, _from=None, paths=None, pull_secret=None):
        """
        V1ImageSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            '_from': 'V1ObjectReference',
            'paths': 'list[V1ImageSourcePath]',
            'pull_secret': 'V1LocalObjectReference'
        }

        self.attribute_map = {
            '_from': 'from',
            'paths': 'paths',
            'pull_secret': 'pullSecret'
        }

        self.__from = _from
        self._paths = paths
        self._pull_secret = pull_secret

    @property
    def _from(self):
        """
        Gets the _from of this V1ImageSource.
        from is a reference to an ImageStreamTag, ImageStreamImage, or DockerImage to copy source from.

        :return: The _from of this V1ImageSource.
        :rtype: V1ObjectReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this V1ImageSource.
        from is a reference to an ImageStreamTag, ImageStreamImage, or DockerImage to copy source from.

        :param _from: The _from of this V1ImageSource.
        :type: V1ObjectReference
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")

        self.__from = _from

    @property
    def paths(self):
        """
        Gets the paths of this V1ImageSource.
        paths is a list of source and destination paths to copy from the image.

        :return: The paths of this V1ImageSource.
        :rtype: list[V1ImageSourcePath]
        """
        return self._paths

    @paths.setter
    def paths(self, paths):
        """
        Sets the paths of this V1ImageSource.
        paths is a list of source and destination paths to copy from the image.

        :param paths: The paths of this V1ImageSource.
        :type: list[V1ImageSourcePath]
        """
        if paths is None:
            raise ValueError("Invalid value for `paths`, must not be `None`")

        self._paths = paths

    @property
    def pull_secret(self):
        """
        Gets the pull_secret of this V1ImageSource.
        pullSecret is a reference to a secret to be used to pull the image from a registry If the image is pulled from the OpenShift registry, this field does not need to be set.

        :return: The pull_secret of this V1ImageSource.
        :rtype: V1LocalObjectReference
        """
        return self._pull_secret

    @pull_secret.setter
    def pull_secret(self, pull_secret):
        """
        Sets the pull_secret of this V1ImageSource.
        pullSecret is a reference to a secret to be used to pull the image from a registry If the image is pulled from the OpenShift registry, this field does not need to be set.

        :param pull_secret: The pull_secret of this V1ImageSource.
        :type: V1LocalObjectReference
        """

        self._pull_secret = pull_secret

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
        if not isinstance(other, V1ImageSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
