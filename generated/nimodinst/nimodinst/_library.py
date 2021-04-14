# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import threading

from nimodinst._visatype import *  # noqa: F403,H303


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niModInst_CloseInstalledDevicesSession_cfunc = None
        self.niModInst_GetExtendedErrorInfo_cfunc = None
        self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc = None
        self.niModInst_GetInstalledDeviceAttributeViString_cfunc = None
        self.niModInst_OpenInstalledDevicesSession_cfunc = None

    def niModInst_CloseInstalledDevicesSession(self, handle):  # noqa: N802
        with self._func_lock:
            if self.niModInst_CloseInstalledDevicesSession_cfunc is None:
                try:
                    self.niModInst_CloseInstalledDevicesSession_cfunc = self._library.niModInst_CloseInstalledDevicesSession
                except AttributeError as e:
                    raise AttributeError("Function niModInst_CloseInstalledDevicesSession was not found in the NI-ModInst runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niModInst_CloseInstalledDevicesSession_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niModInst_CloseInstalledDevicesSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niModInst_CloseInstalledDevicesSession_cfunc(handle)

    def niModInst_GetExtendedErrorInfo(self, error_info_buffer_size, error_info):  # noqa: N802
        with self._func_lock:
            if self.niModInst_GetExtendedErrorInfo_cfunc is None:
                try:
                    self.niModInst_GetExtendedErrorInfo_cfunc = self._library.niModInst_GetExtendedErrorInfo
                except AttributeError as e:
                    raise AttributeError("Function niModInst_GetExtendedErrorInfo was not found in the NI-ModInst runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niModInst_GetExtendedErrorInfo_cfunc.argtypes = [ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niModInst_GetExtendedErrorInfo_cfunc.restype = ViStatus  # noqa: F405
        return self.niModInst_GetExtendedErrorInfo_cfunc(error_info_buffer_size, error_info)

    def niModInst_GetInstalledDeviceAttributeViInt32(self, handle, index, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc is None:
                try:
                    self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc = self._library.niModInst_GetInstalledDeviceAttributeViInt32
                except AttributeError as e:
                    raise AttributeError("Function niModInst_GetInstalledDeviceAttributeViInt32 was not found in the NI-ModInst runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc(handle, index, attribute_id, attribute_value)

    def niModInst_GetInstalledDeviceAttributeViString(self, handle, index, attribute_id, attribute_value_buffer_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niModInst_GetInstalledDeviceAttributeViString_cfunc is None:
                try:
                    self.niModInst_GetInstalledDeviceAttributeViString_cfunc = self._library.niModInst_GetInstalledDeviceAttributeViString
                except AttributeError as e:
                    raise AttributeError("Function niModInst_GetInstalledDeviceAttributeViString was not found in the NI-ModInst runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niModInst_GetInstalledDeviceAttributeViString_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niModInst_GetInstalledDeviceAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niModInst_GetInstalledDeviceAttributeViString_cfunc(handle, index, attribute_id, attribute_value_buffer_size, attribute_value)

    def niModInst_OpenInstalledDevicesSession(self, driver, handle, device_count):  # noqa: N802
        with self._func_lock:
            if self.niModInst_OpenInstalledDevicesSession_cfunc is None:
                try:
                    self.niModInst_OpenInstalledDevicesSession_cfunc = self._library.niModInst_OpenInstalledDevicesSession
                except AttributeError as e:
                    raise AttributeError("Function niModInst_OpenInstalledDevicesSession was not found in the NI-ModInst runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niModInst_OpenInstalledDevicesSession_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViSession), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niModInst_OpenInstalledDevicesSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niModInst_OpenInstalledDevicesSession_cfunc(driver, handle, device_count)
