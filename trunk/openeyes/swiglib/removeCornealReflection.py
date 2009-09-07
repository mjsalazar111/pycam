# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.36
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _removeCornealReflection
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


PI = _removeCornealReflection.PI

def remove_corneal_reflection(*args):
  """
    remove_corneal_reflection(IplImage image, IplImage threshold_image, int sx, int sy, 
        int window_size, int biggest_crr, int crx, 
        int cry, int crr, int valid_point_calc)
    """
  return _removeCornealReflection.remove_corneal_reflection(*args)

def locate_corneal_reflection(*args):
  """
    locate_corneal_reflection(IplImage image, IplImage threshold_image, int sx, int sy, 
        int window_size, int biggest_crar, int crx, 
        int cry, int crar, int valid_point_calc)
    """
  return _removeCornealReflection.locate_corneal_reflection(*args)

def fit_circle_radius_to_corneal_reflection(*args):
  """
    fit_circle_radius_to_corneal_reflection(IplImage image, int cx, int cy, int crar, int biggest_crar, 
        double sin_array, double cos_array, 
        int array_len, int valid_point_calc) -> int
    """
  return _removeCornealReflection.fit_circle_radius_to_corneal_reflection(*args)

def interpolate_corneal_reflection(*args):
  """
    interpolate_corneal_reflection(IplImage image, int cx, int cy, int crr, double sin_array, 
        double cos_array, int array_len, int valid_point_calc)
    """
  return _removeCornealReflection.interpolate_corneal_reflection(*args)

