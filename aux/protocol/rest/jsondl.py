

class JSONDL(object):

    def __init__(self, jsondl_url=None, jsondl_data=None):
        pass


    def __attrMethod(self, method):
        class MethodCaller(object):
            #TODO: This implementation is horrible improve both code and apijson
            def __init__(self, ssp_instance, method):
                self.ssp_instance = ssp_instance
                api_instance = self.ssp_instance.api
                self.method = method
                self.data = dict([('request', dict()),
                                   ('response', dict())])
                requestparams = self.method.get('def').get('params')
                responsetype = self.method.get('def').get('returnType').get('type')
                types = api_instance[self.method['src']].get('types')
                requesttypes = [t.get('type').get('type')  for t in requestparams]
                # annotationtypes = [t.get('type').get('type') for t in [a.get('annotations') for a in requesttypes][0]]
                for _type in types:
                    if _type == responsetype:
                        self.data['response'] = json.loads(types[_type])
                    if _type in requesttypes:
                        self.data['request'] = json.loads(types[_type])
                    # TODO: BUG: not in types definition
                    # if _type in annotationtypes:
                    #     print "annotation"
                    #     print types[_type]
                mappingkey = 'org.springframework.web.bind.annotation.RequestMapping'
                self.requestMapping = self.method.get('def').get('annotations').get(mappingkey)
                
            def __call__(self, kwargs={}):
                request_json = dict()
                #### Validation
                type_mapping = {'string': str,
                                'boolean': bool,
                                'string': str,
                                'null': None,
                                'integer': int,
                                'character': chr,
                                'double': long,
                                'float': float,
                                'complex': complex}
                properties = self.data['request'].get('properties')
                if properties is not None:
                    for prop in properties:
                        # if kwargs.get(prop, False) != False:
                        #     if type_mapping[properties[prop].get('type')] == type(kwargs[prop]):
                        #         print "right type %s" % type(kwargs[prop])
                        #     else:
                        #         print "wrong type %s expected %s" % (type(kwargs[prop]),properties[prop].get('type'))
                        request_json[prop] = kwargs.get(prop, None)
                #TODO: make a validation log with properties
                method = self.requestMapping.get('properties').get('method')[0]
                path = self.requestMapping.get('properties').get('value')[0]
                #Query String builder
                for key in request_json.keys():
                    if key in path:
                        path = path.replace('{'+key+'}', str(kwargs[key]))
                # print path
                response = http.http_send(method,
                                          self.ssp_instance.get_proxy(path),
                                          self.ssp_instance.headers,
                                          json.dumps(request_json),
                                          None)
                return response
        return MethodCaller(self, method)
        
    def __getattr__(self, attr):
        method = self.api_methods.get(attr, None)
        if method is not None:
            return self.__attrMethod(method) 
        else:
            emsg = "%s object has no attribute '%s'" % (self.__class__.__name__,
                                                        attr)
            raise AttributeError(emsg)
    
