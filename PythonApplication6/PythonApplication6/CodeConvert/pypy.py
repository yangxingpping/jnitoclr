#!/usr/bin/env python
# -*- coding: utf-8 -*-
import JNIType as jniType

class Demo(object):
    def GetVersion(self,strx):
        pass;

    def DefineClass(self,strx):
        pass;

    def FindClass(self,strx):
        if strx.find('"') != -1:    #说明FindClass函数参数是字符串
            ClassType = self.objectMap[strx.split('=')[0]][0]
            self.objectMap[strx.split('=')[0]] = (ClassType, strx.split('"')[1].split('/')[-1])
            return ''
        else:                       #说明参数是字符串变量
            pass;
        pass;

    def FromReflectedMethod(self,strx):
        pass;

    def FromReflectedField(self,strx):
        pass;

    def ToReflectedMethod(self,strx):
        pass;

    def GetSuperclass(self,strx):
        pass;

    def IsAssignableFrom(self,strx):
        pass;

    def ToReflectedField(self,strx):
        pass;

    def Throw(self,strx):
        pass;

    def ThrowNew(self,strx):
        pass;

    def ExceptionOccurred(self,strx):
        pass;

    def ExceptionDescribe(self,strx):
        pass;

    def ExceptionClear(self,strx):
        pass;

    def FatalError(self,strx):
        pass;

    def PushLocalFrame(self,strx):
        pass;

    def PopLocalFrame(self,strx):
        pass;

    def NewGlobalRef(self,strx):
        pass;

    def DeleteGlobalRef(self,strx):
        pass;

    def DeleteLocalRef(self,strx):
        pass;

    def IsSameObject(self,strx):
        pass;

    def NewLocalRef(self,strx):
        pass;

    def EnsureLocalCapacity(self,strx):
        pass;

    def AllocObject(self,strx):
        pass;

    def NewObject(self,strx):
        EqualLeft = strx.split('=')[0]  #变量名称
        ClassName = self.objectMap[strx.split('(')[1].split(',')[0]]
        outputState = '%s^ %s = gcnew %s;'%(ClassName[1], EqualLeft, ClassName[1])
        #self.functionSatesList.append(outputState)
        return outputState
        pass;

    def NewObjectV(self,strx):
        pass;

    def NewObjectA(self,strx):
        pass;

    def GetObjectClass(self,strx):
        pass;

    def IsInstanceOf(self,strx):
        pass;

    def GetMethodID(self,strx):
        equalLeft = strx.split('=')[0]
        functionName = strx.split('(')[1].split('"')[1]
        functiontuple = self.objectMap[equalLeft]
        functiontuple = (functiontuple[0],functionName)
        self.objectMap[equalLeft] = functiontuple
        return ''

    def CallObjectMethod(self,strx):
        pass;

    def CallObjectMethodV(self,strx):
        pass;

    def CallObjectMethodA(self,strx):
        pass;

    def CallBooleanMethod(self,strx):
        equalLeft = ''
        equalRight = ''
        if strx.find('=')!=-1:
            equalLeft = strx[:strx.find('=')]
            equalRight=strx[strx.find('=')+1:]
        else:
            equalRight=strx
        strRet = ''
        if equalLeft!='':
            strRet = 'unsiged int %s = '%(equalLeft,)
        strRet += self.CallVoidMethod(equalRight)
        return strRet
        

    def CallBooleanMethodV(self,strx):
        pass;

    def CallBooleanMethodA(self,strx):
        pass;

    def CallByteMethod(self,strx):
        pass;

    def CallByteMethodV(self,strx):
        pass;

    def CallByteMethodA(self,strx):
        pass;

    def CallCharMethod(self,strx):
        pass;

    def CallCharMethodV(self,strx):
        pass;

    def CallCharMethodA(self,strx):
        pass;

    def CallShortMethod(self,strx):
        pass;

    def CallShortMethodV(self,strx):
        pass;

    def CallShortMethodA(self,strx):
        pass;

    def CallIntMethod(self,strx):
        pass;

    def CallIntMethodV(self,strx):
        pass;

    def CallIntMethodA(self,strx):
        pass;

    def CallLongMethod(self,strx):
        pass;

    def CallLongMethodV(self,strx):
        pass;

    def CallLongMethodA(self,strx):
        pass;

    def CallFloatMethod(self,strx):
        pass;

    def CallFloatMethodV(self,strx):
        pass;

    def CallFloatMethodA(self,strx):
        pass;

    def CallDoubleMethod(self,strx):
        pass;

    def CallDoubleMethodV(self,strx):
        pass;

    def CallDoubleMethodA(self,strx):
        pass;

    def CallVoidMethod(self,strx):
        strAfterLeftColon = strx[strx.find('(')+1:]
        objName = strAfterLeftColon.split(',')[0]
        methodobj  = strAfterLeftColon.split(',')[1]
        paramList = '(' + strAfterLeftColon.split(',')[2]
        outputState = '%s->%s%s'%(objName, self.objectMap[methodobj][1], paramList) 
        #self.functionSatesList.append(outputState)
        return outputState;


    def CallVoidMethodV(self,strx):
        pass;

    def CallVoidMethodA(self,strx):
        pass;

    def CallNonvirtualObjectMethod(self,strx):
        pass;

    def CallNonvirtualObjectMethodV(self,strx):
        pass;

    def CallNonvirtualObjectMethodA(self,strx):
        pass;

    def CallNonvirtualBooleanMethod(self,strx):
        pass;

    def CallNonvirtualBooleanMethodV(self,strx):
        pass;

    def CallNonvirtualBooleanMethodA(self,strx):
        pass;

    def CallNonvirtualByteMethod(self,strx):
        pass;

    def CallNonvirtualByteMethodV(self,strx):
        pass;

    def CallNonvirtualByteMethodA(self,strx):
        pass;

    def CallNonvirtualCharMethod(self,strx):
        pass;

    def CallNonvirtualCharMethodV(self,strx):
        pass;

    def CallNonvirtualCharMethodA(self,strx):
        pass;

    def CallNonvirtualShortMethod(self,strx):
        pass;

    def CallNonvirtualShortMethodV(self,strx):
        pass;

    def CallNonvirtualShortMethodA(self,strx):
        pass;

    def CallNonvirtualIntMethod(self,strx):
        pass;

    def CallNonvirtualIntMethodV(self,strx):
        pass;

    def CallNonvirtualIntMethodA(self,strx):
        pass;

    def CallNonvirtualLongMethod(self,strx):
        pass;

    def CallNonvirtualLongMethodV(self,strx):
        pass;

    def CallNonvirtualLongMethodA(self,strx):
        pass;

    def CallNonvirtualFloatMethod(self,strx):
        pass;

    def CallNonvirtualFloatMethodV(self,strx):
        pass;

    def CallNonvirtualFloatMethodA(self,strx):
        pass;

    def CallNonvirtualDoubleMethod(self,strx):
        pass;

    def CallNonvirtualDoubleMethodV(self,strx):
        pass;

    def CallNonvirtualDoubleMethodA(self,strx):
        pass;

    def CallNonvirtualVoidMethod(self,strx):
        pass;

    def CallNonvirtualVoidMethodV(self,strx):
        pass;

    def CallNonvirtualVoidMethodA(self,strx):
        pass;

    def GetFieldID(self,strx):
        pass;

    def GetObjectField(self,strx):
        pass;

    def GetBooleanField(self,strx):
        pass;

    def GetByteField(self,strx):
        pass;

    def GetCharField(self,strx):
        pass;

    def GetShortField(self,strx):
        pass;

    def GetIntField(self,strx):
        pass;

    def GetLongField(self,strx):
        pass;

    def GetFloatField(self,strx):
        pass;

    def GetDoubleField(self,strx):
        pass;

    def SetObjectField(self,strx):
        pass;

    def SetBooleanField(self,strx):
        pass;

    def SetByteField(self,strx):
        pass;

    def SetCharField(self,strx):
        pass;

    def SetShortField(self,strx):
        pass;

    def SetIntField(self,strx):
        pass;

    def SetLongField(self,strx):
        pass;

    def SetFloatField(self,strx):
        pass;

    def SetDoubleField(self,strx):
        pass;

    def GetStaticMethodID(self,strx):
        pass;

    def CallStaticObjectMethod(self,strx):
        pass;

    def CallStaticObjectMethodV(self,strx):
        pass;

    def CallStaticObjectMethodA(self,strx):
        pass;

    def CallStaticBooleanMethod(self,strx):
        pass;

    def CallStaticBooleanMethodV(self,strx):
        pass;

    def CallStaticBooleanMethodA(self,strx):
        pass;

    def CallStaticByteMethod(self,strx):
        pass;

    def CallStaticByteMethodV(self,strx):
        pass;

    def CallStaticByteMethodA(self,strx):
        pass;

    def CallStaticCharMethod(self,strx):
        pass;

    def CallStaticCharMethodV(self,strx):
        pass;

    def CallStaticCharMethodA(self,strx):
        pass;

    def CallStaticShortMethod(self,strx):
        pass;

    def CallStaticShortMethodV(self,strx):
        pass;

    def CallStaticShortMethodA(self,strx):
        pass;

    def CallStaticIntMethod(self,strx):
        pass;

    def CallStaticIntMethodV(self,strx):
        pass;

    def CallStaticIntMethodA(self,strx):
        pass;

    def CallStaticLongMethod(self,strx):
        pass;

    def CallStaticLongMethodV(self,strx):
        pass;

    def CallStaticLongMethodA(self,strx):
        pass;

    def CallStaticFloatMethod(self,strx):
        pass;

    def CallStaticFloatMethodV(self,strx):
        pass;

    def CallStaticFloatMethodA(self,strx):
        pass;

    def CallStaticDoubleMethod(self,strx):
        pass;

    def CallStaticDoubleMethodV(self,strx):
        pass;

    def CallStaticDoubleMethodA(self,strx):
        pass;

    def CallStaticVoidMethod(self,strx):
        pass;

    def CallStaticVoidMethodV(self,strx):
        pass;

    def CallStaticVoidMethodA(self,strx):
        pass;

    def GetStaticFieldID(self,strx):
        pass;

    def GetStaticObjectField(self,strx):
        pass;

    def GetStaticBooleanField(self,strx):
        pass;

    def GetStaticByteField(self,strx):
        pass;

    def GetStaticCharField(self,strx):
        pass;

    def GetStaticShortField(self,strx):
        pass;

    def GetStaticIntField(self,strx):
        pass;

    def GetStaticLongField(self,strx):
        pass;

    def GetStaticFloatField(self,strx):
        pass;

    def GetStaticDoubleField(self,strx):
        pass;

    def SetStaticObjectField(self,strx):
        pass;

    def SetStaticBooleanField(self,strx):
        pass;

    def SetStaticByteField(self,strx):
        pass;

    def SetStaticCharField(self,strx):
        pass;

    def SetStaticShortField(self,strx):
        pass;

    def SetStaticIntField(self,strx):
        pass;

    def SetStaticLongField(self,strx):
        pass;

    def SetStaticFloatField(self,strx):
        pass;

    def SetStaticDoubleField(self,strx):
        pass;

    def NewString(self,strx):
        pass;

    def GetStringLength(self,strx):
        pass;

    def GetStringChars(self,strx):
        pass;

    def ReleaseStringChars(self,strx):
        pass;

    def NewStringUTF(self,strx):
        equalLeft = strx.split('=')[0]
        param = strx[strx.find('('):]
        outputState = 'System::String^ %s = gcnew System::String%s' %(equalLeft, param)
        #self.functionSatesList.append(outputState)
        return outputState


    def GetStringUTFLength(self,strx):
        pass;

    def GetStringUTFChars(self,strx):
        equalLeft = strx.split('=')[0]
        objInfo = self.objectMap[equalLeft]
        jstr = strx[strx.find('(')+1:].split(',')[0]
        objInfo = (objInfo[0], jstr)
        self.objectMap[equalLeft]  = objInfo
        param = strx[strx.find('('):]
        outputState = '%s %s = marshal_as<std::string>(%s);' %(objInfo[0], equalLeft,jstr)
        #self.functionSatesList.append(outputState)
        return outputState
        pass;

    def ReleaseStringUTFChars(self,strx):
        pass;

    def GetArrayLength(self,strx):
        pass;

    def NewObjectArray(self,strx):
        pass;

    def GetObjectArrayElement(self,strx):
        pass;

    def SetObjectArrayElement(self,strx):
        pass;

    def NewBooleanArray(self,strx):
        pass;

    def NewByteArray(self,strx):
        pass;

    def NewCharArray(self,strx):
        pass;

    def NewShortArray(self,strx):
        pass;

    def NewIntArray(self,strx):
        pass;

    def NewLongArray(self,strx):
        pass;

    def NewFloatArray(self,strx):
        pass;

    def NewDoubleArray(self,strx):
        pass;

    def GetBooleanArrayElements(self,strx):
        pass;

    def GetByteArrayElements(self,strx):
        pass;

    def GetCharArrayElements(self,strx):
        pass;

    def GetShortArrayElements(self,strx):
        pass;

    def GetIntArrayElements(self,strx):
        pass;

    def GetLongArrayElements(self,strx):
        pass;

    def GetFloatArrayElements(self,strx):
        pass;

    def GetDoubleArrayElements(self,strx):
        pass;

    def ReleaseBooleanArrayElements(self,strx):
        pass;

    def ReleaseByteArrayElements(self,strx):
        pass;

    def ReleaseCharArrayElements(self,strx):
        pass;

    def ReleaseShortArrayElements(self,strx):
        pass;

    def ReleaseIntArrayElements(self,strx):
        pass;

    def ReleaseLongArrayElements(self,strx):
        pass;

    def ReleaseFloatArrayElements(self,strx):
        pass;

    def ReleaseDoubleArrayElements(self,strx):
        pass;

    def GetBooleanArrayRegion(self,strx):
        pass;

    def GetByteArrayRegion(self,strx):
        pass;

    def GetCharArrayRegion(self,strx):
        pass;

    def GetShortArrayRegion(self,strx):
        pass;

    def GetIntArrayRegion(self,strx):
        pass;

    def GetLongArrayRegion(self,strx):
        pass;

    def GetFloatArrayRegion(self,strx):
        pass;

    def GetDoubleArrayRegion(self,strx):
        pass;

    def SetBooleanArrayRegion(self,strx):
        pass;

    def SetByteArrayRegion(self,strx):
        pass;

    def SetCharArrayRegion(self,strx):
        pass;

    def SetShortArrayRegion(self,strx):
        pass;

    def SetIntArrayRegion(self,strx):
        pass;

    def SetLongArrayRegion(self,strx):
        pass;

    def SetFloatArrayRegion(self,strx):
        pass;

    def SetDoubleArrayRegion(self,strx):
        pass;

    def RegisterNatives(self,strx):
        pass;

    def UnregisterNatives(self,strx):
        pass;

    def MonitorEnter(self,strx):
        pass;

    def MonitorExit(self,strx):
        pass;

    def GetJavaVM(self,strx):
        pass;

    def GetStringRegion(self,strx):
        pass;

    def GetStringUTFRegion(self,strx):
        pass;

    def GetPrimitiveArrayCritical(self,strx):
        pass;

    def ReleasePrimitiveArrayCritical(self,strx):
        pass;

    def GetStringCritical(self,strx):
        pass;

    def ReleaseStringCritical(self,strx):
        pass;

    def NewWeakGlobalRef(self,strx):
        pass;

    def DeleteWeakGlobalRef(self,strx):
        pass;

    def ExceptionCheck(self,strx):
        pass;

    def NewDirectByteBuffer(self,strx):
        pass;

    def GetDirectBufferAddress(self,strx):
        pass;

    def GetDirectBufferCapacity(self,strx):
        pass;

    def GetObjectRefType(self,strx):
        pass;      
    def __init__(self, pathIn, passOut):
        self.filepathIn = pathIn                    #输入的cpp文件路径
        self.filepathOut = passOut                  #输出的cpp文件路径
        self.functionSignature = ''                 #jni函数定义的签名
        self.functionSatesList = []                 #输出语句的链表
        self.functionToRetureMap={'FindClass':'jclass', 'NewObject':'jobject',
                                  'GetStringUTFChars':'const char*', 'GetMethodID':'jmethodID',
                                  'CallBooleanMethod':'jboolean', 'DeleteLocalRef':'void'}
        self.FunctionToMethodName={"SetObjectArrayElement":Demo.SetObjectArrayElement,
            "GetLongArrayRegion":Demo.GetLongArrayRegion,
            "CallNonvirtualIntMethod":Demo.CallNonvirtualIntMethod,
            "NewObject":Demo.NewObject,
            "GetCharArrayRegion":Demo.GetCharArrayRegion,
            "ReleaseLongArrayElements":Demo.ReleaseLongArrayElements,
            "CallNonvirtualObjectMethod":Demo.CallNonvirtualObjectMethod,
            "GetStaticMethodID":Demo.GetStaticMethodID,
            "CallStaticDoubleMethodV":Demo.CallStaticDoubleMethodV,
            "ReleaseIntArrayElements":Demo.ReleaseIntArrayElements,
            "DefineClass":Demo.DefineClass,
            "CallNonvirtualBooleanMethodV":Demo.CallNonvirtualBooleanMethodV,
            "CallNonvirtualBooleanMethodA":Demo.CallNonvirtualBooleanMethodA,
            "NewObjectArray":Demo.NewObjectArray,
            "GetStaticByteField":Demo.GetStaticByteField,
            "GetArrayLength":Demo.GetArrayLength,
            "MonitorExit":Demo.MonitorExit,
            "CallObjectMethodA":Demo.CallObjectMethodA,
            "GetBooleanField":Demo.GetBooleanField,
            "SetBooleanArrayRegion":Demo.SetBooleanArrayRegion,
            "PopLocalFrame":Demo.PopLocalFrame,
            "GetStaticFloatField":Demo.GetStaticFloatField,
            "SetCharField":Demo.SetCharField,
            "ReleaseCharArrayElements":Demo.ReleaseCharArrayElements,
            "SetCharArrayRegion":Demo.SetCharArrayRegion,
            "CallNonvirtualObjectMethodA":Demo.CallNonvirtualObjectMethodA,
            "SetStaticShortField":Demo.SetStaticShortField,
            "SetBooleanField":Demo.SetBooleanField,
            "CallLongMethodV":Demo.CallLongMethodV,
            "GetStaticDoubleField":Demo.GetStaticDoubleField,
            "CallNonvirtualByteMethodA":Demo.CallNonvirtualByteMethodA,
            "CallNonvirtualFloatMethodA":Demo.CallNonvirtualFloatMethodA,
            "CallStaticCharMethod":Demo.CallStaticCharMethod,
            "GetJavaVM":Demo.GetJavaVM,
            "DeleteLocalRef":Demo.DeleteLocalRef,
            "GetStringChars":Demo.GetStringChars,
            "FromReflectedField":Demo.FromReflectedField,
            "CallDoubleMethod":Demo.CallDoubleMethod,
            "NewDirectByteBuffer":Demo.NewDirectByteBuffer,
            "CallStaticBooleanMethodV":Demo.CallStaticBooleanMethodV,
            "ThrowNew":Demo.ThrowNew,
            "SetShortField":Demo.SetShortField,
            "CallNonvirtualLongMethodA":Demo.CallNonvirtualLongMethodA,
            "GetMethodID":Demo.GetMethodID,
            "SetIntField":Demo.SetIntField,
            "ReleaseBooleanArrayElements":Demo.ReleaseBooleanArrayElements,
            "CallNonvirtualObjectMethodV":Demo.CallNonvirtualObjectMethodV,
            "CallStaticIntMethod":Demo.CallStaticIntMethod,
            "GetShortArrayRegion":Demo.GetShortArrayRegion,
            "GetStaticCharField":Demo.GetStaticCharField,
            "ReleaseByteArrayElements":Demo.ReleaseByteArrayElements,
            "SetShortArrayRegion":Demo.SetShortArrayRegion,
            "CallBooleanMethodV":Demo.CallBooleanMethodV,
            "ReleaseStringChars":Demo.ReleaseStringChars,
            "GetLongArrayElements":Demo.GetLongArrayElements,
            "CallNonvirtualBooleanMethod":Demo.CallNonvirtualBooleanMethod,
            "DeleteWeakGlobalRef":Demo.DeleteWeakGlobalRef,
            "CallNonvirtualDoubleMethod":Demo.CallNonvirtualDoubleMethod,
            "FromReflectedMethod":Demo.FromReflectedMethod,
            "GetIntArrayRegion":Demo.GetIntArrayRegion,
            "MonitorEnter":Demo.MonitorEnter,
            "CallObjectMethod":Demo.CallObjectMethod,
            "GetObjectRefType":Demo.GetObjectRefType,
            "CallNonvirtualDoubleMethodV":Demo.CallNonvirtualDoubleMethodV,
            "CallNonvirtualIntMethodV":Demo.CallNonvirtualIntMethodV,
            "NewDoubleArray":Demo.NewDoubleArray,
            "CallStaticObjectMethodA":Demo.CallStaticObjectMethodA,
            "CallNonvirtualLongMethod":Demo.CallNonvirtualLongMethod,
            "GetBooleanArrayElements":Demo.GetBooleanArrayElements,
            "CallStaticIntMethodA":Demo.CallStaticIntMethodA,
            "CallVoidMethodA":Demo.CallVoidMethodA,
            "UnregisterNatives":Demo.UnregisterNatives,
            "CallStaticDoubleMethod":Demo.CallStaticDoubleMethod,
            "CallStaticLongMethodA":Demo.CallStaticLongMethodA,
            "CallBooleanMethodA":Demo.CallBooleanMethodA,
            "CallIntMethodV":Demo.CallIntMethodV,
            "GetStaticFieldID":Demo.GetStaticFieldID,
            "CallVoidMethodV":Demo.CallVoidMethodV,
            "ExceptionDescribe":Demo.ExceptionDescribe,
            "GetSuperclass":Demo.GetSuperclass,
            "GetFloatField":Demo.GetFloatField,
            "GetByteField":Demo.GetByteField,
            "GetIntField":Demo.GetIntField,
            "CallIntMethodA":Demo.CallIntMethodA,
            "GetShortField":Demo.GetShortField,
            "CallLongMethodA":Demo.CallLongMethodA,
            "CallShortMethodV":Demo.CallShortMethodV,
            "CallNonvirtualVoidMethod":Demo.CallNonvirtualVoidMethod,
            "GetDirectBufferAddress":Demo.GetDirectBufferAddress,
            "SetDoubleField":Demo.SetDoubleField,
            "NewString":Demo.NewString,
            "ReleaseStringCritical":Demo.ReleaseStringCritical,
            "SetStaticObjectField":Demo.SetStaticObjectField,
            "CallStaticBooleanMethodA":Demo.CallStaticBooleanMethodA,
            "CallShortMethodA":Demo.CallShortMethodA,
            "CallStaticLongMethod":Demo.CallStaticLongMethod,
            "CallNonvirtualShortMethodA":Demo.CallNonvirtualShortMethodA,
            "SetStaticBooleanField":Demo.SetStaticBooleanField,
            "CallNonvirtualByteMethod":Demo.CallNonvirtualByteMethod,
            "SetFloatField":Demo.SetFloatField,
            "CallStaticDoubleMethodA":Demo.CallStaticDoubleMethodA,
            "CallNonvirtualLongMethodV":Demo.CallNonvirtualLongMethodV,
            "CallStaticByteMethodA":Demo.CallStaticByteMethodA,
            "NewWeakGlobalRef":Demo.NewWeakGlobalRef,
            "GetObjectField":Demo.GetObjectField,
            "GetStaticBooleanField":Demo.GetStaticBooleanField,
            "NewFloatArray":Demo.NewFloatArray,
            "CallStaticFloatMethod":Demo.CallStaticFloatMethod,
            "ToReflectedMethod":Demo.ToReflectedMethod,
            "CallStaticShortMethodV":Demo.CallStaticShortMethodV,
            "ReleaseStringUTFChars":Demo.ReleaseStringUTFChars,
            "GetDoubleField":Demo.GetDoubleField,
            "CallNonvirtualCharMethodV":Demo.CallNonvirtualCharMethodV,
            "NewGlobalRef":Demo.NewGlobalRef,
            "GetBooleanArrayRegion":Demo.GetBooleanArrayRegion,
            "SetByteArrayRegion":Demo.SetByteArrayRegion,
            "CallStaticVoidMethod":Demo.CallStaticVoidMethod,
            "GetCharField":Demo.GetCharField,
            "CallVoidMethod":Demo.CallVoidMethod,
            "CallNonvirtualShortMethod":Demo.CallNonvirtualShortMethod,
            "ToReflectedField":Demo.ToReflectedField,
            "SetIntArrayRegion":Demo.SetIntArrayRegion,
            "CallDoubleMethodV":Demo.CallDoubleMethodV,
            "SetLongArrayRegion":Demo.SetLongArrayRegion,
            "CallDoubleMethodA":Demo.CallDoubleMethodA,
            "CallNonvirtualCharMethodA":Demo.CallNonvirtualCharMethodA,
            "FindClass":Demo.FindClass,
            "NewIntArray":Demo.NewIntArray,
            "CallObjectMethodV":Demo.CallObjectMethodV,
            "SetStaticByteField":Demo.SetStaticByteField,
            "GetByteArrayRegion":Demo.GetByteArrayRegion,
            "CallStaticVoidMethodA":Demo.CallStaticVoidMethodA,
            "GetVersion":Demo.GetVersion,
            "CallStaticBooleanMethod":Demo.CallStaticBooleanMethod,
            "CallShortMethod":Demo.CallShortMethod,
            "GetStaticShortField":Demo.GetStaticShortField,
            "GetByteArrayElements":Demo.GetByteArrayElements,
            "CallStaticObjectMethod":Demo.CallStaticObjectMethod,
            "CallNonvirtualFloatMethod":Demo.CallNonvirtualFloatMethod,
            "CallStaticObjectMethodV":Demo.CallStaticObjectMethodV,
            "IsSameObject":Demo.IsSameObject,
            "CallNonvirtualFloatMethodV":Demo.CallNonvirtualFloatMethodV,
            "GetFloatArrayRegion":Demo.GetFloatArrayRegion,
            "CallByteMethod":Demo.CallByteMethod,
            "PushLocalFrame":Demo.PushLocalFrame,
            "CallCharMethodA":Demo.CallCharMethodA,
            "SetStaticIntField":Demo.SetStaticIntField,
            "SetLongField":Demo.SetLongField,
            "ExceptionOccurred":Demo.ExceptionOccurred,
            "GetFieldID":Demo.GetFieldID,
            "GetFloatArrayElements":Demo.GetFloatArrayElements,
            "SetByteField":Demo.SetByteField,
            "GetIntArrayElements":Demo.GetIntArrayElements,
            "SetFloatArrayRegion":Demo.SetFloatArrayRegion,
            "CallFloatMethod":Demo.CallFloatMethod,
            "GetStaticObjectField":Demo.GetStaticObjectField,
            "CallNonvirtualByteMethodV":Demo.CallNonvirtualByteMethodV,
            "SetDoubleArrayRegion":Demo.SetDoubleArrayRegion,
            "CallStaticShortMethodA":Demo.CallStaticShortMethodA,
            "GetCharArrayElements":Demo.GetCharArrayElements,
            "Throw":Demo.Throw,
            "NewLongArray":Demo.NewLongArray,
            "GetStaticIntField":Demo.GetStaticIntField,
            "AllocObject":Demo.AllocObject,
            "ReleasePrimitiveArrayCritical":Demo.ReleasePrimitiveArrayCritical,
            "CallStaticIntMethodV":Demo.CallStaticIntMethodV,
            "GetStringUTFRegion":Demo.GetStringUTFRegion,
            "CallLongMethod":Demo.CallLongMethod,
            "CallStaticFloatMethodA":Demo.CallStaticFloatMethodA,
            "GetStringRegion":Demo.GetStringRegion,
            "GetObjectArrayElement":Demo.GetObjectArrayElement,
            "CallNonvirtualDoubleMethodA":Demo.CallNonvirtualDoubleMethodA,
            "GetObjectClass":Demo.GetObjectClass,
            "CallStaticLongMethodV":Demo.CallStaticLongMethodV,
            "CallStaticCharMethodV":Demo.CallStaticCharMethodV,
            "CallStaticVoidMethodV":Demo.CallStaticVoidMethodV,
            "CallFloatMethodV":Demo.CallFloatMethodV,
            "CallBooleanMethod":Demo.CallBooleanMethod,
            "CallStaticCharMethodA":Demo.CallStaticCharMethodA,
            "NewBooleanArray":Demo.NewBooleanArray,
            "CallNonvirtualVoidMethodV":Demo.CallNonvirtualVoidMethodV,
            "GetDoubleArrayRegion":Demo.GetDoubleArrayRegion,
            "GetStringLength":Demo.GetStringLength,
            "ReleaseFloatArrayElements":Demo.ReleaseFloatArrayElements,
            "ExceptionClear":Demo.ExceptionClear,
            "ReleaseShortArrayElements":Demo.ReleaseShortArrayElements,
            "CallFloatMethodA":Demo.CallFloatMethodA,
            "SetObjectField":Demo.SetObjectField,
            "CallIntMethod":Demo.CallIntMethod,
            "CallStaticShortMethod":Demo.CallStaticShortMethod,
            "IsAssignableFrom":Demo.IsAssignableFrom,
            "NewObjectA":Demo.NewObjectA,
            "CallNonvirtualIntMethodA":Demo.CallNonvirtualIntMethodA,
            "GetStaticLongField":Demo.GetStaticLongField,
            "SetStaticFloatField":Demo.SetStaticFloatField,
            "RegisterNatives":Demo.RegisterNatives,
            "NewCharArray":Demo.NewCharArray,
            "GetStringUTFChars":Demo.GetStringUTFChars,
            "CallNonvirtualShortMethodV":Demo.CallNonvirtualShortMethodV,
            "CallStaticByteMethod":Demo.CallStaticByteMethod,
            "NewObjectV":Demo.NewObjectV,
            "SetStaticDoubleField":Demo.SetStaticDoubleField,
            "CallNonvirtualCharMethod":Demo.CallNonvirtualCharMethod,
            "NewLocalRef":Demo.NewLocalRef,
            "GetStringCritical":Demo.GetStringCritical,
            "NewStringUTF":Demo.NewStringUTF,
            "CallCharMethodV":Demo.CallCharMethodV,
            "SetStaticCharField":Demo.SetStaticCharField,
            "SetStaticLongField":Demo.SetStaticLongField,
            "GetPrimitiveArrayCritical":Demo.GetPrimitiveArrayCritical,
            "NewByteArray":Demo.NewByteArray,
            "EnsureLocalCapacity":Demo.EnsureLocalCapacity,
            "GetLongField":Demo.GetLongField,
            "NewShortArray":Demo.NewShortArray,
            "DeleteGlobalRef":Demo.DeleteGlobalRef,
            "CallStaticFloatMethodV":Demo.CallStaticFloatMethodV,
            "ExceptionCheck":Demo.ExceptionCheck,
            "ReleaseDoubleArrayElements":Demo.ReleaseDoubleArrayElements,
            "GetDirectBufferCapacity":Demo.GetDirectBufferCapacity,
            "CallCharMethod":Demo.CallCharMethod,
            "CallByteMethodA":Demo.CallByteMethodA,
            "IsInstanceOf":Demo.IsInstanceOf,
            "GetStringUTFLength":Demo.GetStringUTFLength,
            "CallByteMethodV":Demo.CallByteMethodV,
            "FatalError":Demo.FatalError,
            "CallNonvirtualVoidMethodA":Demo.CallNonvirtualVoidMethodA,
            "GetShortArrayElements":Demo.GetShortArrayElements,
            "CallStaticByteMethodV":Demo.CallStaticByteMethodV,
            "GetDoubleArrayElements":Demo.GetDoubleArrayElements,
            }
        self.objectMap  ={}                         #所有对象到类类型的映射
        self.ClassToMethod={}                      #所有类型到函数集的映射                         
       # self.classSet = set([])                     #需要使用的java类的集合
       # self.methodSet=set([])                      #需要调用的函数名称集合
        self.classMap = {}                           #需要使用的java类的集合（key为class名，value为class的方法的set)
        self.outputStream = []                      #输出文件的临时保存数组
        self.functionCommit=''                      #函数声明的注释
    
    #函数功能：把一行语句中的所有完整注释去掉
    #函数参数:linex --需要去掉注释的句子
    #函数返回：去掉注释后的句子
    def FilterCommit(self, linex):
        stringTemp = ''
        commitIndexF = linex.find('/*')
        commitIndexS = linex.find('//')
        if commitIndexF != -1 and commitIndexS!=-1:
            if commitIndexF<commitIndexS: # /* // ....
                if linex.find('*/')!=-1: #  /* // */
                    stringTemp += linex[:commitIndexF]
                    if len(linex)>linex.find('*/'):
                        stringTemp += linex[linex.find('*/')+2:]
                else:       #       /* // commit
                    pass;                         
            else: # // /*
                pass;
                        
        elif commitIndexF != -1:
            if linex.find('*/')==-1:        # /*
                stringTemp += linex[:commitIndexF]
            else :          # /* */
                stringTemp += linex[:commitIndexF]
                stringTemp += linex[linex.find('*/')+2:]
        elif commitIndexS != -1:
            stringTemp += linex[:commitIndexS]
        else:
            stringTemp = linex;
        return stringTemp

    def ProcessFile(self):     
        with open(self.filepathIn, 'r') as f:
            tempNodeType = ''
            tempNodeMap = {}                                #临时保存查找到的一个完整节点(函数查找，函数调用)的信息(主要是为了获取函数名称)
            stringTemp  = ''                                #临时保存所有未处理的节点所有行
            for linex in f.readlines():
                linexStrip = linex.strip('\t')
                commitIndexF = linex.find('/*')
                commitIndexS = linex.find('//')
                if tempNodeMap.get('{',0)>0:                      #这是在一个函数定义中，进行下面处理
                    if commitIndexF != -1 and commitIndexS!=-1:
                        if commitIndexF<commitIndexS: # /* // ....
                            if linex.find('*/')!=-1: #  /* // */
                                stringTemp += linex[:commitIndexF]
                                if len(linex)>linex.find('*/'):
                                    stringTemp += linex[linex.find('*/')+2:]
                            else:       #       /* // commit
                                tempNodeType='commit'                          
                        else: # // /*
                            pass;
                        
                    elif commitIndexF != -1:
                        if linex.find('*/')==-1:        # /*
                            stringTemp += linex[:commitIndexF]
                            tempNodeType = 'commit'
                        else :          # /* */
                            stringTemp += linex[:commitIndexF]
                            stringTemp += linex[linex.find('*/')+2:]

                    elif commitIndexS != -1:
                        stringTemp += linex[:commitIndexS]
                        pass;
                    else:
                        if tempNodeType!='commit':      #此行是有效语句
                            stringTemp += linex
                            tempNodeMap['{'] = tempNodeMap.get('{',0) + linex.count('{')
                            tempNodeMap['}'] = tempNodeMap.get('}',0) + linex.count('}')
                            if tempNodeMap.get('{')>0 and (tempNodeMap['{'] == tempNodeMap['}']):
                                self.processOneFunction(stringTemp)
                                stringTemp=''
                                tempNodeMap.clear()
                                self.functionSignature = ''
                        else:           #此行是注释的一部分
                            if linex.find('*/')!=-1:        #/**/注释结束,注意，注释行后面不能添加任何语句
                                tempNodeType=''
 
                else:           #在一个函数的定义之外，或者一个函数的开始
                    if linex.startswith('JNIEXPORT'):
                        tempNodeType = 'functionSignature'
                        self.functionSignature += linex
                    elif tempNodeType=='functionSignature':
                        openbrackcount = linex.find('{')
                        if(openbrackcount>0):
                            self.functionSignature += linex[:openbrackcount]
                            #stringTemp += linex[openbrackcount:]
                            stringTemp += self.FilterCommit(linex[openbrackcount:])
                            tempNodeMap['{'] = tempNodeMap.get('{',0)+linex.count('{')
                            tempNodeType = ''

                        else:
                            self.functionSignature += linex
                    else:   #这是函数申明的注释
                        self.functionCommit += linex
                        pass;

            with open(self.filepathOut, 'w') as fo:
                for it in self.functionSatesList:        #把输出写到文件中
                    fo.write(it)
                    fo.write('\n')
    
    #函数功能：把一个jni函数定义转换成CLR定义
    #函数参数:stringOneFunction(in)jni函数定义完整字符串
    #函数返回：...
    def processOneFunction(self, stringOneFunction):    
        tempNodeType = ''
        stringTemp = ''  
        for linex in stringOneFunction.split('\n'):
            OneLine = stringTemp + linex +'\n'
            stringTemp = OneLine

            braceIndexL = OneLine.find('{')
            braceIndexR = OneLine.find('}')
            semicolon   = OneLine.find(';')
            colonIndex  = OneLine.find(':')
            while braceIndexL != -1 or braceIndexR != -1 or semicolon != -1:
                stringTemp = ''
                minNumber = min(x for x in (semicolon, braceIndexL, braceIndexR, colonIndex) if x>-1)
                self.processOneNode(OneLine[:minNumber+1])
                OneLine = OneLine[minNumber+1:]
                braceIndexL = OneLine.find('{')
                braceIndexR = OneLine.find('}')
                semicolon   = OneLine.find(';')
                colonIndex  = OneLine.find(':')
             
      
    #函数功能：把一条jni语句转换成CLR定义（；结尾的语句，{和}暂时不支持注释语句)
    #函数参数:stringOneNode(in)jni语句字符串
    #函数返回：...
    def processOneNode(self, stringOneNode):   
        if stringOneNode.find('{')!=-1:   #有左大括号，需要分别对左括号的左边调用processOneNode,然后把{写入outputStream，再对{的右边调用processOneNode
            #if len(stringOneNode.replace(' ','').split('{')[0])>0:
            #    processOneNode(self, stringOneNode.replace(' ','').split('{')[0])
            #    pass;
              self.functionSatesList.append('{')
                #if len(stringOneNode.replace(' ','').split('{')[1])>0:
                #    processOneNode(stringOneNode.replace(' ','').split('{')[1])
                #    pass;
                #else:
                #    pass;
        elif stringOneNode.find('}') != -1:
            #if len(stringOneNode.replace(' ','').split('}')[0])>0:
            #    processOneNode(self, stringOneNode.replace(' ','').split('}')[0])
            #    pass;
             #self.outputStream += '}'
             self.functionSatesList.append('}')
            #    if len(stringOneNode.replace(' ','').split('}')[1])>0:
            #        processOneNode(stringOneNode.replace(' ','').split('}')[1])
            #        pass;
            #    else:
            #        pass;
            #pass;
        else:       #以分号（; :)结尾的句子
            NodeStrip = stringOneNode.replace('\n', '')
            NodeStrip = NodeStrip.replace('\t', ' ')
            NodeStrip = NodeStrip.lstrip(' ')
           # NodeStrip = NodeStrip.lstrip('\t')
            equalLeft = NodeStrip.split('=')[0].strip(' ')
            firstItem =equalLeft[:equalLeft.find(equalLeft.split(' ')[-1])].strip(' ')
            if firstItem in jniType.JNIType:            #这是一条声明语句
                NodeStrip  = NodeStrip.replace(firstItem,'')
                NodeStrip  = NodeStrip.lstrip(' ')
                self.objectMap[NodeStrip.split(' ')[0]]=(firstItem,'')
            else:
                pass;
            if NodeStrip.find('env->') !=-1:                #这是一条jni语句,不包括jclass
                NodeStrip = NodeStrip.replace(' ', '')
                FunctionName = NodeStrip[NodeStrip.find('env->')+len('env->'):].split('(')[0]  #获取函数名
                callFunc = self.FunctionToMethodName.get(FunctionName,'')
                if callFunc != '':
                    NodeStrip = NodeStrip.replace(' ', '')
                    stateAlqaz = self.FunctionToMethodName[FunctionName](self,NodeStrip)  #从map中找到对应函数调用的处理函数并调用
                    if stateAlqaz != '':
                        self.functionSatesList.append(stateAlqaz)
                pass;
            else:      #正常的c++语句
                #self.outputStream += stringOneNode;
                self.functionSatesList.append(stringOneNode)
                pass;
    

