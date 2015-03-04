JNIEXPORT jobject JNICALL
Java_com_yuandian_cc
(JNIEnv *env, jobject, 
jstring queryid_jstr) { 
	jobject udpsession_list_obj  = env->NewObject(class_list, list_init);
	jclass class_list = env->FindClass("java/util/ArrayList");
	jmethodID list_init  = env->GetMethodID(class_list, "<init>", "()V");
	jmethodID list_init_add = env->GetMethodID(class_list, "add", "zzzzz");
	
	
	jclass item = env->FindClass("java/util/item");
	jmethodID item_init_add = env->GetMethodID(item, "Fn", "zzzzz");
	jobject    udpsession_obj  = env->NewObject(item, item_init);
	jstring	   jstrItem = env->NewStringUTF(unit->cde.c_str());
	
	env->CallVoidMethod(udpsession_obj, item_init_add, jstrItem);
	
	env->CallBooleanMethod(udpsession_list_obj, list_init_add, udpsession_obj);
	
	int next/*def */;
	func(a,//cde
	b,/*whate*/
	c,/*fj
	mi*/
	d);
	if (xyz=1
	)
		int abc =32;
	switch(ebc):
	{
		case 1:
			;
			break;
		default:
			break;
	}
	return nullptr;
	/*multiline commit in one line*/
	/*multiline commit in 
	multiline 
	*/	
}

// JNIEXPORT jobject JNICALL
// Java_com_yuandian_second
// (JNIEnv *env, jobject, jstring queryid_jstr){	
	// return nullptr;
	// /*multiline commit in one line*/
	// /*multiline commit in 
	// //multiline 
	// */
// }