chunked_message='''HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Thu, 26 Feb 2015 14:38:37 GMT
Content-Type: text/xml;charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Application-Context: application:8080

1f09
<?xml version="1.0" encoding="UTF-8" standalone="no"?><wsdl:definitions xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:sch0="http://kezzlerssp.com/schemas/kcengine" xmlns:sch1="http://kezzlerssp.com/schemas/security" xmlns:sch2="http://kezzlerssp.com/schemas/common" xmlns:sch3="http://kezzlerssp.com/schema/metadata/foreign/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://kezzlerssp.com/schemas/kcengine" targetNamespace="http://kezzlerssp.com/schemas/kcengine">
  <wsdl:types>
    <xs:schema xmlns="http://kezzlerssp.com/schemas/kcengine" xmlns:ns0="http://kezzlerssp.com/schemas/common" xmlns:ns1="http://kezzlerssp.com/schemas/security" xmlns:ns2="http://kezzlerssp.com/schema/metadata/foreign/" xmlns:xs="http://www.w3.org/2001/XMLSchema" attributeFormDefault="unqualified" elementFormDefault="qualified" targetNamespace="http://kezzlerssp.com/schemas/kcengine"><xs:import namespace="http://kezzlerssp.com/schemas/common"/><xs:import namespace="http://kezzlerssp.com/schemas/security"/><xs:import namespace="http://kezzlerssp.com/schemas/common"/><xs:import namespace="http://kezzlerssp.com/schemas/common"/><xs:import namespace="http://kezzlerssp.com/schemas/common"/><xs:import namespace="http://kezzlerssp.com/schemas/common"/><xs:import namespace="http://kezzlerssp.com/schema/metadata/foreign/"/><xs:import namespace="http://kezzlerssp.com/schemas/security"/><xs:import namespace="http://kezzlerssp.com/schemas/security"/><xs:import namespace="http://kezzlerssp.com/schemas/common"/><xs:import namespace="http://kezzlerssp.com/schemas/security"/><xs:import namespace="http://kezzlerssp.com/schemas/common"/><xs:import namespace="http://kezzlerssp.com/schemas/security"/><xs:import namespace="http://kezzlerssp.com/schemas/common"/><xs:element name="ListCodePatternsRequest"><xs:annotation><xs:documentation>Request a list of all available code types that can be ordered.</xs:documentation></xs:annotation><xs:complexType/></xs:element><xs:element name="ListCodePatternsResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codePattern"><xs:complexType><xs:attribute name="id" type="xs:string" use="required"><xs:annotation><xs:documentation>The ID of the code pattern</xs:documentation></xs:annotation></xs:attribute><xs:attribute name="description" type="xs:string" use="required"><xs:annotation><xs:documentation>A text description of the code pattern</xs:documentation></xs:annotation></xs:attribute><xs:attribute name="minLength" type="xs:positiveInteger" use="required"><xs:annotation><xs:documentation>The minimum code length that can be ordered</xs:documentation></xs:annotation></xs:attribute><xs:attribute name="defaultLength" type="xs:positiveInteger" use="required"><xs:annotation><xs:documentation>The default code length of this code pattern</xs:documentation></xs:annotation></xs:attribute><xs:attribute name="maxLength" type="xs:positiveInteger" use="required"><xs:annotation><xs:documentation>The maximum code length allowed for this code pattern</xs:documentation></xs:annotation></xs:attribute><xs:attribute name="caseSensitive" type="xs:boolean" use="required"><xs:annotation><xs:documentation>Whether this code is case sensitive or not</xs:documentation></xs:annotation></xs:attribute></xs:complexType></xs:element></xs:sequence><xs:attribute name="defaultCase" type="CodeCase" use="required"><xs:annotation><xs:documentation>The default code case if the code is case-insensitive</xs:documentation></xs:annotation></xs:attribute></xs:complexType></xs:element><xs:element name="ListOrdersRequest"><xs:annotation><xs:documentation>Request a list of all available orders with optional filtering offset and maximum number of results.</xs:documentation></xs:annotation><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element minOccurs="0" name="metadataFilter" type="xs:string"><xs:annotation><xs:documentation>A search string that will filter all orders not containing the meta-data
                                    described in the expression.
                                </xs:documentation></xs:annotation></xs:element><xs:element minOccurs="0" name="descriptionFilter" type="xs:string"><xs:annotation><xs:documentation>A search string that will filter all orders not containing the
                                    description search string
                                </xs:documentation></xs:annotation></xs:element></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListOrdersResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="order" type="Order"><xs:annotation><xs:documentation>Zero or more orders</xs:documentation></xs:annotation></xs:element></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="InitOrderRequest"><xs:annotation><xs:documentation>Create a new empty order containing zero codes. Use [expandOrder] to request codes for the order.</xs:documentation></xs:annotation><xs:complexType><xs:sequence><xs:element minOccurs="0" name="type" type="OrderType"><xs:annotation><xs:documentation>Deprecated! Do not use</xs:documentation></xs:annotation></xs:element><xs:element default="false" minOccurs="0" name="sectioned" type="xs:boolean"><xs:annotation><xs:documentation>Should this order be split into section. Usaually used only with pre-printed media</xs:documentation></xs:annotation></xs:element><xs:element minOccurs="0" name="description" type="xs:string"><xs:annotation><xs:documentation>An optional description of the order</xs:documentation></xs:annotation></xs:element><xs:element minOccurs="0" name="productId" type="xs:int"><xs:annotation><xs:documentation>An optional product ID. Has to match a previously registered product ID, see [listProducts]</xs:documentation></xs:annotation></xs:element><xs:element minOccurs="0" name="gtin" type="xs:string"><xs:annotation><xs:documentation>An optional product GTIN. Has to match a previously registered product's GTIN, see [listProducts]</xs:documentation></xs:annotation></xs:element><xs:element minOccurs="0" name="metadataSchema" type="xs:string"><xs:annotation><xs:documentation>An optional meta-data schema ID. Has to match a previously registered schema ID, see [listMetadataSchemas]</xs:documentation></xs:annotation></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="InitOrderResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"><xs:annotation><xs:documentation>The ID of the created order</xs:documentation></xs:annotation></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateOrderRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element minOccurs="0" name="description" nillable="true" type="xs:string"/><xs:element minOccurs="0" name="productId" nillable="true" type="xs:int"/><xs:element minOccurs="0" name="metadataSchema" nillable="true" type="xs:string"/><xs:element minOccurs="0" name="sectioned" type="xs:boolean"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateOrderResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateOrderDataRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element minOccurs="0" name="description" type="xs:string"/><xs:element minOccurs="0" name="productId" type="xs:int"/><xs:element minOccurs="0" name="metadataSchema" type="xs:string"/><xs:element minOccurs="0" name="sectioned" type="xs:boolean"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateOrderDataResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="LockOr
2000
derRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="LockOrderResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadOrderRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadOrderResponse" type="Order"/><xs:element name="ExpandOrderRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="orderSize" type="xs:int"/><xs:element name="codeLength" type="xs:int"/><xs:element name="codePattern" type="CodePattern"/><xs:element minOccurs="0" name="codeCase" type="CodeCase"/><xs:element minOccurs="0" name="sorting" type="CodeSorting"/><xs:element minOccurs="0" name="name" type="ExpansionName"/></xs:sequence></xs:complexType></xs:element><xs:element name="ExpandOrderResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="orderRequestSequence" type="xs:int"/><xs:element name="downloadUrl" type="xs:anyURI"/><xs:element name="expansionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="MultiExpandOrderRequest"><xs:complexType><xs:sequence><xs:element name="expansion"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="orderSize" type="xs:int"/><xs:element name="codeLength" type="xs:int"/><xs:element name="codePattern" type="CodePattern"/><xs:element minOccurs="0" name="codeCase" type="CodeCase"/><xs:element minOccurs="0" name="name" type="ExpansionName"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="pairedExpansion"><xs:complexType><xs:sequence><xs:element name="codeLength" type="xs:int"/><xs:element name="codePattern" type="CodePattern"/><xs:element minOccurs="0" name="codeCase" type="CodeCase"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="repeats" type="xs:positiveInteger"/></xs:sequence></xs:complexType></xs:element><xs:element name="MultiExpandOrderResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" name="expansion"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="orderRequestSequence" type="xs:integer"/><xs:element name="downloadUrl" type="xs:anyURI"/><xs:element name="expansionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="ReadSsccRequest"><xs:complexType><xs:sequence><xs:element name="sscc" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadSsccResponse"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="orderId" type="xs:long"/><xs:element name="codeIndex" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadSsccSequenceRequest"><xs:complexType><xs:sequence><xs:element name="expansionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadSsccSequenceResponse"><xs:complexType><xs:sequence><xs:element name="start" type="xs:long"/><xs:element name="end" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="AddReservedSsccSequenceRequest"><xs:complexType><xs:sequence><xs:element name="start" type="xs:long"/><xs:element name="end" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="AddReservedSsccSequenceResponse"><xs:complexType><xs:sequence><xs:element name="start" type="xs:long"/><xs:element name="end" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteReservedSsccSequenceRequest"><xs:complexType><xs:sequence><xs:element name="start" type="xs:long"/><xs:element name="end" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteReservedSsccSequenceResponse"><xs:complexType><xs:sequence><xs:element name="start" type="xs:long"/><xs:element name="end" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ListReservedSsccSequenceRequest"><xs:complexType/></xs:element><xs:element name="ListReservedSsccSequenceResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="sequence"><xs:complexType><xs:sequence><xs:element name="start" type="xs:long"/><xs:element name="end" type="xs:long"/></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="CreateSsccSequenceRequest"><xs:complexType><xs:sequence><xs:element name="expansionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="CreateSsccSequenceResponse"><xs:complexType><xs:sequence><xs:element name="start" type="xs:long"/><xs:element name="end" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="SetExpansionStatusRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="sequence" type="xs:int"/><xs:element minOccurs="0" name="status" type="ExpansionStatusType"/></xs:sequence></xs:complexType></xs:element><xs:element name="SetExpansionStatusResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="ListExpansionsRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence><xs:attribute name="offset" type="xs:int"/><xs:attribute name="max" type="xs:int"/></xs:complexType></xs:element><xs:element name="ListExpansionsResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="expansion" type="OrderExpansion"/></xs:sequence><xs:attribute name="offset" type="xs:int"/><xs:attribute name="max" type="xs:int"/><xs:attribute name="totalRecords" type="xs:long"/></xs:complexType></xs:element><xs:element name="GetExpansionRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetExpansionResponse" type="OrderExpansion"/><xs:element name="ListAllExpansionsRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element name="startTime" type="xs:dateTime"/><xs:element name="endTime" type="xs:dateTime"/><xs:element minOccurs="0" name="organizationId" type="xs:int"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListAllExpansionsResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="expansion" type="OrderExpansion"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="GetCodesProducedByUserRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element name="startTime" type="xs:dateTime"/><xs:element name="endTime" type="xs:dateTime"/><xs:element minOccurs="0" name="organizationId" type="xs:int"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="GetCodesProducedByUserResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codes" type="CodesPerUser"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="GetCodesProducedByGroupRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element name="startTime" type="xs:dateTime"/><xs:element name="endTime" type="xs:dateTime"/><xs:element minOccurs="0" name="organizationId" type="xs:int"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="GetCodesProducedByGroupResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codes" type="CodesPerGroup"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="GetCodesProducedByProductRequest"><xs:complexType><xs:complexContent><xs:exte
2000
nsion base="ns0:PageRequest"><xs:sequence><xs:element name="startTime" type="xs:dateTime"/><xs:element name="endTime" type="xs:dateTime"/><xs:element minOccurs="0" name="organizationId" type="xs:int"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="GetCodesProducedByProductResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codes" type="CodesPerProduct"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="DownloadCodesRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:choice><xs:element name="expansionId" type="xs:long"/><xs:element name="orderId" type="xs:long"/></xs:choice></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="DownloadCodesResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element minOccurs="0" name="expansionId" type="xs:long"/><xs:element name="codes" type="StringValueList"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListExpansionCodesRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="sequence" type="xs:int"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListExpansionCodesResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="code" type="CodeData"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ExpansionsStatusRequest"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="sequence" type="xs:int"/></xs:sequence><xs:attribute name="orderId" type="xs:long"/></xs:complexType></xs:element><xs:element name="ExpansionsStatusResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="expansionStatus" type="ExpansionStatus"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetOrderExpansionsValidationsRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetOrderExpansionsValidationsResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="expansionValidations" type="ExpansionValidations"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteLastExpansionRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteLastExpansionResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetOrderValidationsRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetOrderValidationsResponse"><xs:complexType><xs:sequence><xs:element name="total" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetOrderCodeStatusStatisticsRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetOrderCodeStatusStatisticsResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="status" type="CodeStatusStatistics"/></xs:sequence></xs:complexType></xs:element><xs:simpleType name="EntryChannelType"><xs:restriction base="xs:string"><xs:enumeration value="SMS"/><xs:enumeration value="WEB"/></xs:restriction></xs:simpleType><xs:simpleType name="StringValueList"><xs:list itemType="xs:string"/></xs:simpleType><xs:simpleType name="CharacterType"><xs:restriction base="xs:string"><xs:pattern value="[a-zA-Z]"/></xs:restriction></xs:simpleType><xs:simpleType name="CodeStatusType"><xs:restriction base="xs:string"><xs:enumeration value="BASIC_8"/><xs:enumeration value="BASIC_16"/><xs:enumeration value="TIMESTAMP_8"/><xs:enumeration value="TIMESTAMP_16"/></xs:restriction></xs:simpleType><xs:complexType name="CodeStatusField"><xs:sequence><xs:element name="id" type="xs:int"/><xs:element minOccurs="0" name="builtin" type="xs:boolean"/><xs:element name="description" type="xs:string"/></xs:sequence><xs:attribute name="validatable" type="xs:boolean"/><xs:attribute name="packable" type="xs:boolean"/><xs:attribute name="settable" type="xs:boolean"/><xs:attribute name="unsettable" type="xs:boolean"/></xs:complexType><xs:complexType name="OutputCode"><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="orderId" type="xs:long"/><xs:element name="codeIndex" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="OtherProductIdType"><xs:sequence><xs:element name="otherProductId" type="xs:string"/></xs:sequence><xs:attribute name="type" type="xs:string"/></xs:complexType><xs:complexType name="ProductSummary"><xs:sequence><xs:element name="productId" type="xs:long"/><xs:element name="name" type="xs:string"/></xs:sequence></xs:complexType><xs:complexType name="Product"><xs:sequence><xs:element name="productId" type="xs:long"/><xs:element name="name" type="xs:string"/><xs:element minOccurs="0" name="gtin" type="xs:string"/><xs:element minOccurs="0" name="otherProductId" type="OtherProductIdType"/><xs:element minOccurs="0" name="alias" type="xs:string"/><xs:element minOccurs="0" name="customerProductReference" type="xs:string"/><xs:element minOccurs="0" name="netWeight" type="xs:decimal"/><xs:element minOccurs="0" name="atiGroupId" type="xs:long"/><xs:element minOccurs="0" name="atiGroupName" type="xs:string"/><xs:element minOccurs="0" name="metadataSchemaId" type="xs:int"/><xs:element minOccurs="0" name="packageTypeId" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="CreateProduct"><xs:sequence><xs:element name="name" type="xs:string"/><xs:element minOccurs="0" name="gtin" type="xs:string"/><xs:element minOccurs="0" name="otherProductId" type="OtherProductIdType"/><xs:element minOccurs="0" name="alias" type="xs:string"/><xs:element minOccurs="0" name="customerProductReference" type="xs:string"/><xs:element minOccurs="0" name="atiGroupId" type="xs:long"/><xs:element minOccurs="0" name="packageTypeId" type="xs:long"/></xs:sequence></xs:complexType><xs:simpleType name="ExpansionStatusType"><xs:restriction base="xs:string"><xs:enumeration value="LFP"/><xs:enumeration value="P"/></xs:restriction></xs:simpleType><xs:simpleType name="CodeCase"><xs:restriction base="xs:string"><xs:enumeration value="UPPERCASE"/><xs:enumeration value="LOWERCASE"/></xs:restriction></xs:simpleType><xs:simpleType name="ShadowCodeStatus"><xs:restriction base="xs:string"><xs:enumeration value="ADMINISTRATIVE"/><xs:enumeration value="CONSUMER"/></xs:restriction></xs:simpleType><xs:complexType name="OrderExpansion"><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="orderId" type="xs:long"/><xs:element name="sequence" type="xs:int"/><xs:element name="codePattern" type="CodePattern"/><xs:element name="sorting" type="CodeSorting"/><xs:element name="orderSize" type="xs:long"/><xs:element name="startIndex" type="xs:long"/><xs:element name="endIndex" type="xs:long"/><xs:element name="codeLength" type="xs:int"/><xs:element name="created" type="xs:dateTime"/><xs:element minOccurs="0" name="started" type="xs:dateTime"/><xs:element minOccurs="0" name="completed" type="xs:dateTime"/><xs:element minOccurs="0" name="removed" type="xs:dateTime"/><xs:element minOccurs="0" name="codeCase" type="CodeCase"/><xs:element minOccurs="0" name="name" type="ExpansionName"/><xs:element minOccurs="0" name="status" type="ExpansionStatusType"/><xs:element minOccurs="0" name="shadowStatus" type="ShadowCodeStatus"/><xs:element minOccurs="0" name="createdBy" type="xs:string"/><xs:element minOccurs="0" name="createdByGroup" type="xs:string"/></xs:seq
2000
uence></xs:complexType><xs:complexType name="CodeData"><xs:sequence><xs:element name="text" type="xs:string"/><xs:element minOccurs="0" name="statuses"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" name="status" type="CodeStatus"/></xs:sequence></xs:complexType></xs:element></xs:sequence><xs:attribute name="index" type="xs:long"/></xs:complexType><xs:simpleType name="CodePattern"><xs:restriction base="xs:string"><xs:minLength value="1"/></xs:restriction></xs:simpleType><xs:simpleType name="ExpansionName"><xs:restriction base="xs:string"><xs:maxLength value="32"/><xs:minLength value="0"/></xs:restriction></xs:simpleType><xs:complexType name="ExpansionStatus"><xs:sequence><xs:element name="sequence" type="xs:int"/><xs:element name="operation" type="xs:string"/><xs:element name="progress" type="xs:double"/></xs:sequence></xs:complexType><xs:complexType name="ExpansionValidations"><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="validations" type="xs:long"/><xs:element name="expansionSize" type="xs:long"/></xs:sequence></xs:complexType><xs:simpleType name="CodeSorting"><xs:restriction base="xs:string"><xs:enumeration value="R"/><xs:enumeration value="A"/><xs:enumeration value="D"/></xs:restriction></xs:simpleType><xs:element name="order" type="Order"/><xs:complexType name="Order"><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="type" type="OrderType"/><xs:element name="size" type="xs:long"/><xs:element name="created" type="xs:dateTime"/><xs:element name="isLocked" type="xs:boolean"/><xs:element minOccurs="0" name="description" type="xs:string"/><xs:element name="owner" type="ns1:SummarySid"/><xs:element minOccurs="0" name="product" type="Product"/><xs:element minOccurs="0" name="metadataSchema" type="xs:string"/><xs:element name="metadataPresent" type="xs:boolean"/><xs:element default="false" minOccurs="0" name="sectioned" type="xs:boolean"/><xs:element minOccurs="0" name="createdBy" type="xs:string"/></xs:sequence></xs:complexType><xs:simpleType name="OrderType"><xs:restriction base="xs:string"><xs:enumeration value="m"/><xs:enumeration value="p"/><xs:enumeration value="s"/></xs:restriction></xs:simpleType><xs:complexType name="SectionCreate"><xs:sequence><xs:element minOccurs="0" name="id" type="xs:long"/><xs:element name="orderId" type="xs:long"/><xs:element name="startIndex" type="xs:long"/><xs:element name="endIndex" type="xs:long"/><xs:element minOccurs="0" name="activateDate" type="xs:dateTime"/><xs:element minOccurs="0" name="deactivateDate" type="xs:dateTime"/><xs:element name="maxValidations" type="xs:integer"/><xs:element name="enabled" type="xs:boolean"/><xs:element minOccurs="0" name="comment" type="xs:string"/><xs:element minOccurs="0" name="productId" type="xs:long"/><xs:element minOccurs="0" name="metadataSchema" type="xs:string"/></xs:sequence></xs:complexType><xs:complexType name="SectionsStatistics"><xs:sequence><xs:element name="activeSections" type="xs:int"/><xs:element name="nonActiveSections" type="xs:int"/><xs:element name="activeCodes" type="xs:long"/><xs:element name="nonActiveCodes" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="Section"><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="orderId" type="xs:long"/><xs:element name="startIndex" type="xs:long"/><xs:element minOccurs="0" name="startCode" type="xs:string"/><xs:element name="endIndex" type="xs:long"/><xs:element minOccurs="0" name="endCode" type="xs:string"/><xs:element minOccurs="0" name="activateDate" type="xs:dateTime"/><xs:element minOccurs="0" name="deactivateDate" type="xs:dateTime"/><xs:element minOccurs="0" name="activateOrderedDate" type="xs:dateTime"/><xs:element minOccurs="0" name="activatedBy" type="ns1:OutputUser"/><xs:element name="maxValidations" type="xs:integer"/><xs:element name="enabled" type="xs:boolean"/><xs:element minOccurs="0" name="comment" type="xs:string"/><xs:element minOccurs="0" name="product" type="Product"/><xs:element minOccurs="0" name="metadataSchema" type="xs:string"/><xs:element minOccurs="0" name="atiCount" type="xs:long"/><xs:element minOccurs="0" name="rollId" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="Roll"><xs:sequence><xs:element name="codesCountInActiveStretches" type="xs:long"/><xs:element name="activeStretchesCount" type="xs:long"/><xs:element name="startIndex" type="xs:long"/><xs:element name="endIndex" type="xs:long"/><xs:element name="tempEndIndex" type="xs:long"/><xs:element name="full" type="xs:boolean"/><xs:element minOccurs="0" name="lastActivationOrdered" type="xs:dateTime"/><xs:element minOccurs="0" name="asc" type="xs:boolean"/></xs:sequence></xs:complexType><xs:complexType name="FullRoll"><xs:sequence><xs:element name="rollId" type="xs:long"/><xs:element name="orderId" type="xs:long"/><xs:element name="ascending" type="xs:boolean"/><xs:element name="startIndex" type="xs:long"/><xs:element name="endIndex" type="xs:long"/><xs:element name="sections"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="section" type="Section"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="unassigned"><xs:complexType><xs:sequence><xs:element name="startIndex" type="xs:long"/><xs:element name="endIndex" type="xs:long"/></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:complexType><xs:complexType name="Ati"><xs:sequence><xs:element minOccurs="0" name="id" type="xs:long"/><xs:element name="name" type="xs:string"/><xs:element name="type" type="AtiType"/><xs:element name="webMessage" type="xs:string"/><xs:element name="smsMessage" type="xs:string"/><xs:element name="translations" type="AtiTranslations"/><xs:element minOccurs="0" name="activate" type="xs:string"/><xs:element minOccurs="0" name="deactivate" type="xs:string"/><xs:element name="validationsRangeStart" type="xs:int"/><xs:element minOccurs="0" name="validationsRangeEnd" type="xs:int"/></xs:sequence></xs:complexType><xs:complexType name="AtiTranslations"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="translation"><xs:complexType><xs:sequence><xs:element name="country" type="xs:string"/><xs:element minOccurs="0" name="webMessage" type="xs:string"/><xs:element minOccurs="0" name="smsMessage" type="xs:string"/></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:complexType><xs:complexType name="AttachedAti"><xs:complexContent><xs:extension base="Ati"><xs:sequence><xs:element name="isActive" type="xs:boolean"/><xs:element minOccurs="0" name="activeFrom" type="xs:dateTime"/><xs:element minOccurs="0" name="activeTo" type="xs:dateTime"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType><xs:complexType name="AtiGroup"><xs:sequence><xs:element minOccurs="0" name="id" type="xs:long"/><xs:element name="name" type="xs:string"/><xs:element name="atis"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="ati" type="Ati"/></xs:sequence></xs:complexType></xs:element></xs:sequence><xs:attribute default="false" name="default" type="xs:boolean" use="optional"/></xs:complexType><xs:complexType name="InputAtiGroup"><xs:sequence><xs:element minOccurs="0" name="id" type="xs:long"/><xs:element name="name" type="xs:string"/><xs:element name="atiIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element></xs:sequence><xs:attribute default="false" name="default" type="xs:boolean" use="optional"/></xs:complexType><xs:simpleType name="AtiType"><xs:restriction base="xs:string"><xs:enumeration value="f"/><xs:enumeration value="w"/><xs:enumeration value="n"/></xs:restriction></xs:simpleType><xs:complexType name="MetadataSchemaDescription"><xs:sequence><xs:element name="organization" type="xs:string"/><xs:element name="name" type="xs:string"/><xs:element name="isDefault" type="xs:boolean"/><xs:element name="content" type="xs:string"/></xs:sequence><xs:attribute name="id" type="xs:int" use="optional"/></xs:complexType><xs:complexType name="ProductMetadataSchemaDescription"><xs:sequence><xs:element name="id" type="xs:int"/><xs:element name=
2000
"name" type="xs:string"/><xs:element name="content" type="xs:string"/></xs:sequence></xs:complexType><xs:complexType name="SimpleCodeConfigSummary"><xs:simpleContent><xs:extension base="xs:positiveInteger"><xs:attribute name="pattern" type="xs:string" use="optional"/></xs:extension></xs:simpleContent></xs:complexType><xs:complexType name="EntryChannelSummary"><xs:simpleContent><xs:extension base="xs:string"><xs:attribute name="id" type="xs:int" use="required"/><xs:attribute name="type" type="xs:string" use="required"/></xs:extension></xs:simpleContent></xs:complexType><xs:complexType name="ValidationLogEntry"><xs:all><xs:element name="code" type="xs:string"/><xs:element name="channel" type="EntryChannelSummary"/><xs:element name="entry" type="xs:string"/><xs:element minOccurs="0" name="organization"><xs:complexType><xs:simpleContent><xs:extension base="xs:string"><xs:attribute name="id" type="xs:int"/></xs:extension></xs:simpleContent></xs:complexType></xs:element><xs:element name="user"><xs:complexType><xs:simpleContent><xs:extension base="xs:string"><xs:attribute name="id" type="xs:int"/></xs:extension></xs:simpleContent></xs:complexType></xs:element><xs:element minOccurs="0" name="userExtraInformation" type="UserExtraInformation"/><xs:element minOccurs="0" name="location"><xs:complexType><xs:sequence><xs:element name="country" type="xs:string"/><xs:element minOccurs="0" name="name" type="xs:string"/><xs:element minOccurs="0" name="coords"><xs:complexType><xs:attribute name="lat" type="xs:decimal"/><xs:attribute name="long" type="xs:decimal"/></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="occurred" type="xs:dateTime"/><xs:element minOccurs="0" name="orderId" type="xs:long"/><xs:element minOccurs="0" name="sectionId" type="xs:long"/><xs:element minOccurs="0" name="product" type="Product"/><xs:element minOccurs="0" name="validations" type="xs:int"/><xs:element minOccurs="0" name="maxValidations" type="xs:int"/><xs:element minOccurs="0" name="errorCode" type="xs:int"/><xs:element name="valid" type="xs:string"/></xs:all></xs:complexType><xs:complexType name="UserExtraInformation"><xs:sequence><xs:element minOccurs="0" name="phoneNumber" type="xs:string"/><xs:element minOccurs="0" name="email" type="xs:string"/></xs:sequence></xs:complexType><xs:complexType name="CodeStatusStatistics"><xs:sequence><xs:element name="id" type="xs:int"/><xs:element name="name" type="CodeStatus"/><xs:element name="count" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="CodeStatusSnapshot"><xs:sequence><xs:element name="statusId" type="xs:int"/><xs:element name="orderId" type="xs:long"/><xs:element name="count" type="xs:long"/><xs:element name="modified" type="xs:dateTime"/></xs:sequence></xs:complexType><xs:complexType name="CodeStatus"><xs:simpleContent><xs:extension base="xs:string"><xs:attribute name="id" type="xs:int"/></xs:extension></xs:simpleContent></xs:complexType><xs:simpleType name="CodeStatusFilterOperator"><xs:restriction base="xs:string"><xs:enumeration value="SET"/><xs:enumeration value="UNSET"/></xs:restriction></xs:simpleType><xs:complexType name="SectionValidations"><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="validations" type="xs:long"/><xs:element name="sectionSize" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="BatchValidationEntry"><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="status" type="xs:string"/><xs:element minOccurs="0" name="orderId" type="xs:long"/><xs:element minOccurs="0" name="sectionId" type="xs:long"/><xs:element minOccurs="0" name="validations" type="xs:int"/><xs:element minOccurs="0" name="maxValidations" type="xs:int"/></xs:sequence></xs:complexType><xs:simpleType name="ValidationType"><xs:restriction base="xs:string"><xs:enumeration value="NORMAL"/><xs:enumeration value="SUPERVISED"/></xs:restriction></xs:simpleType><xs:simpleType name="ValidationCountRelation"><xs:restriction base="xs:string"><xs:enumeration value="EXACTLY"/><xs:enumeration value="AT_LEAST"/><xs:enumeration value="AT_MOST"/></xs:restriction></xs:simpleType><xs:complexType name="ValidationsLogFilter"><xs:all><xs:element minOccurs="0" name="organizationId" type="xs:int"/><xs:element minOccurs="0" name="hideValid" type="xs:boolean"/><xs:element minOccurs="0" name="hideInvalid" type="xs:boolean"/><xs:element minOccurs="0" name="hideVerified" type="xs:boolean"/><xs:element minOccurs="0" name="occurredAfter" type="xs:dateTime"/><xs:element minOccurs="0" name="occurredBefore" type="xs:dateTime"/><xs:element minOccurs="0" name="codes"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="code" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="codeSimilarity" type="xs:float"/><xs:element minOccurs="0" name="ignoreCodeCase" type="xs:boolean"/><xs:element minOccurs="0" name="ips"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="ip" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="phoneNumbers"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="phoneNumber" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="orderIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="sectionIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="productIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="productId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="validationCount" type="ValidationCount"/><xs:element minOccurs="0" name="channelIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="channelId" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="validationType" type="ValidationType"/></xs:all><xs:attribute name="offset" type="xs:int" use="required"/><xs:attribute name="max" type="xs:positiveInteger" use="required"/></xs:complexType><xs:complexType name="ValidationCount"><xs:sequence><xs:element name="count" type="xs:int"/><xs:element name="relation" type="ValidationCountRelation"/></xs:sequence></xs:complexType><xs:complexType name="CodesPerUser"><xs:sequence><xs:element name="user" type="xs:string"/><xs:element name="codesCount" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="CodesPerGroup"><xs:sequence><xs:element name="group" type="xs:string"/><xs:element name="codesCount" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="CodesPerProduct"><xs:sequence><xs:element name="product" type="xs:string"/><xs:element name="codesCount" type="xs:long"/></xs:sequence></xs:complexType><xs:element name="ListProductsRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"/></xs:complexContent></xs:complexType></xs:element><xs:element name="ListProductsResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="product" type="Product"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="CreateProductRequest"><xs:complexType><xs:sequence><xs:element name="product" type="CreateProduct"/></xs:sequence></xs:complexType></xs:element><xs:element name="CreateProductResponse"><xs:complexType><xs:sequence><xs:element name="productId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateProductRequest"><xs:complexType><xs:sequence><xs:element name="product" type="Product"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateProductResponse"><xs:complexType><xs:sequence><xs:element name="productId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element 
2000
name="DeleteProductRequest"><xs:complexType><xs:sequence><xs:element name="productId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteProductResponse"><xs:complexType><xs:sequence><xs:element name="productId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetProductRequest"><xs:complexType><xs:sequence><xs:choice><xs:element name="productId" type="xs:long"/><xs:element name="gtin" type="xs:string"/><xs:element name="otherProductId" type="xs:string"/><xs:element name="customerProductReference" type="xs:string"/><xs:element name="alias" type="xs:string"/></xs:choice></xs:sequence></xs:complexType></xs:element><xs:element name="GetProductResponse"><xs:complexType><xs:sequence><xs:element name="product" type="Product"/></xs:sequence></xs:complexType></xs:element><xs:element name="FindLookAlikeCodeRequest"><xs:annotation><xs:documentation>Used by support/operators to attempt to find a correct code by analyzing matches excluding typical typos</xs:documentation></xs:annotation><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"><xs:annotation><xs:documentation>The code to search for</xs:documentation></xs:annotation></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="FindLookAlikeCodeResponse"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"><xs:annotation><xs:documentation>The code that was searched for</xs:documentation></xs:annotation></xs:element><xs:element name="validCodes"><xs:annotation><xs:documentation>A list of codes that are similar and valid</xs:documentation></xs:annotation><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="code" type="OutputCode"/></xs:sequence><xs:attribute name="count" type="xs:int" use="required"/></xs:complexType></xs:element><xs:element name="verifiedCodes"><xs:annotation><xs:documentation>A list of codes that are similar and correct codes but not activated</xs:documentation></xs:annotation><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="code" type="OutputCode"/></xs:sequence><xs:attribute name="count" type="xs:int" use="required"/></xs:complexType></xs:element></xs:sequence><xs:attribute name="permutationsSearched" type="xs:int" use="required"><xs:annotation><xs:documentation>The number of permutations of the original code searched</xs:documentation></xs:annotation></xs:attribute></xs:complexType></xs:element><xs:element name="ListCodeConfigsRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"/></xs:complexContent></xs:complexType></xs:element><xs:element name="ListCodeConfigsResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codeConfig" type="CodeConfigSummary"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ReadCodeConfigRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadCodeConfigResponse" type="CodeConfig"/><xs:element name="CreateCodeConfigRequest" type="CodeConfig"/><xs:element name="CreateCodeConfigResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:complexType name="CodeConfigSummary"><xs:sequence><xs:element minOccurs="0" name="id" type="xs:int"><xs:annotation><xs:documentation>The ID of the code code configuration</xs:documentation></xs:annotation></xs:element><xs:element name="description" type="xs:string"><xs:annotation><xs:documentation>A text description of the code configuration</xs:documentation></xs:annotation></xs:element><xs:element name="defaultCodeLength" type="xs:positiveInteger"><xs:annotation><xs:documentation>The default code length of this code pattern</xs:documentation></xs:annotation></xs:element><xs:element name="minCodeLength" type="xs:positiveInteger"><xs:annotation><xs:documentation>The minimum code length allowed for this code pattern</xs:documentation></xs:annotation></xs:element><xs:element name="maxCodeLength" type="xs:positiveInteger"><xs:annotation><xs:documentation>The maximum code length allowed for this code pattern</xs:documentation></xs:annotation></xs:element><xs:element name="alphabet"><xs:annotation><xs:documentation>The possible characters in the code</xs:documentation></xs:annotation><xs:complexType><xs:simpleContent><xs:extension base="xs:string"><xs:attribute name="charCount" type="xs:int" use="required"/></xs:extension></xs:simpleContent></xs:complexType></xs:element></xs:sequence></xs:complexType><xs:complexType name="CodeConfig"><xs:complexContent><xs:extension base="CodeConfigSummary"><xs:sequence><xs:element name="rLen" type="xs:int"/><xs:element name="cLen" type="xs:int"/><xs:element name="sLen" type="xs:int"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType><xs:element name="CreateSectionRequest" type="SectionCreate"/><xs:element name="CreateSectionResponse"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadSectionRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadSectionResponse" type="Section"/><xs:element name="UpdateSectionRequest" type="SectionCreate"/><xs:element name="UpdateSectionResponse"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteSectionRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteSectionResponse"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ListSectionsRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListSectionsResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element name="statistics" type="SectionsStatistics"/><xs:element maxOccurs="unbounded" minOccurs="0" name="section" type="Section"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListAtisRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence/></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListAtisResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="ati" type="Ati"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListSectionAtisRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ListSectionAtisResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="ati" type="AttachedAti"/></xs:sequence></xs:complexType></xs:element><xs:element name="AddAtiRequest" type="Ati"/><xs:element name="AddAtiResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateAtiRequest" type="Ati"/><xs:element name="UpdateAtiResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteAtiRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteAtiResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadAtiRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="
2000
ReadAtiResponse" type="Ati"/><xs:element name="UnlinkAtiRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="UnlinkAtiResponse"><xs:complexType/></xs:element><xs:element name="UnlinkAllAtisRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="UnlinkAllAtisResponse"><xs:complexType/></xs:element><xs:element name="ApplyAtiRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ApplyAtiResponse"><xs:complexType/></xs:element><xs:element name="ApplyAtiTemplateGroupRequest"><xs:annotation><xs:documentation>Unsupported. Use ApplyAtiRequest instead</xs:documentation></xs:annotation><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ApplyAtiTemplateGroupResponse"><xs:complexType/></xs:element><xs:element name="RenameAtiRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="name" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="RenameAtiResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetOrderSectionsValidationsRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetOrderSectionsValidationsResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="sectionValidations" type="SectionValidations"/></xs:sequence></xs:complexType></xs:element><xs:element name="MapExpansionsToSectionsRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="MapExpansionsToSectionsResponse"><xs:complexType/></xs:element><xs:element name="ListAtiGroupsRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence/></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListAtiGroupsResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="atiGroup" type="AtiGroup"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="AddAtiGroupRequest" type="InputAtiGroup"/><xs:element name="AddAtiGroupResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ApplyAtiGroupRequest"><xs:complexType><xs:sequence><xs:element name="atiGroupId" type="xs:long"/><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ApplyAtiGroupResponse"><xs:complexType/></xs:element><xs:element name="ReadAtiGroupRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadAtiGroupResponse" type="AtiGroup"/><xs:element name="DefaultAtiGroupRequest"><xs:complexType/></xs:element><xs:element name="DefaultAtiGroupResponse"><xs:complexType><xs:sequence><xs:element minOccurs="0" name="defaultAtiGroup" type="AtiGroup"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateAtiGroupRequest" type="InputAtiGroup"/><xs:element name="UpdateAtiGroupResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteAtiGroupRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteAtiGroupResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ActivateSectionRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/><xs:element minOccurs="0" name="activateDate" type="xs:dateTime"/><xs:element minOccurs="0" name="productId" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element name="ActivateSectionResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="DeactivateSectionRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/><xs:element minOccurs="0" name="activateDate" type="xs:dateTime"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeactivateSectionResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="IdentifyRollRequest"><xs:complexType><xs:sequence><xs:element minOccurs="0" name="cfgId" type="xs:int"/><xs:element name="code" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="IdentifyRollResponse"><xs:complexType><xs:sequence><xs:element name="rollId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ActivateRollSectionRequest"><xs:complexType><xs:sequence><xs:element name="rollId" type="xs:long"/><xs:element minOccurs="0" name="cfgId" type="xs:int"/><xs:element minOccurs="0" name="code" type="xs:string"/><xs:element name="productId" type="xs:long"/><xs:element name="metadataSchemaId" type="xs:int"/><xs:element name="metadata" type="xs:string"/><xs:element minOccurs="0" name="activationDate" type="xs:dateTime"/></xs:sequence></xs:complexType></xs:element><xs:element name="ActivateRollSectionResponse"><xs:complexType><xs:sequence><xs:element name="rollId" type="xs:long"/><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetRollRequest"><xs:complexType><xs:sequence><xs:element name="rollId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetRollResponse"><xs:complexType><xs:sequence><xs:element name="roll" type="FullRoll"/></xs:sequence></xs:complexType></xs:element><xs:element name="CalibrateRollRequest"><xs:complexType><xs:sequence><xs:element minOccurs="0" name="cfgId" type="xs:int"/><xs:element name="firstCode" type="xs:string"/><xs:element name="secondCode" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="CalibrateRollResponse"><xs:complexType><xs:sequence><xs:element name="rollId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadRollRequest"><xs:complexType><xs:sequence><xs:element name="rollId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadRollResponse" type="Roll"/><xs:element name="MarkTemporaryRollEndRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/><xs:element name="temporaryEndIndex" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="MarkTemporaryRollEndResponse" type="Roll"/><xs:element name="CreateNewSectionInRollRequest"><xs:complexType><xs:sequence><xs:element name="rollId" type="xs:long"/><xs:element minOccurs="0" name="activateDate" type="xs:dateTime"/><xs:element minOccurs="0" name="productId" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element name="CreateNewSectionInRollResponse" type="Section"/><xs:element name="DeActivateSectionInRollRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeActivateSectionInRollResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="DeleteOrderMetadataRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteOrderMetadataResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteOrderSectionMetadataRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:e
2000
lement name="DeleteOrderSectionMetadataResponse"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ListMetadataSchemasRequest"><xs:complexType><xs:sequence><xs:element minOccurs="0" name="organizationId" type="xs:int"/></xs:sequence><xs:attribute name="offset" type="xs:integer"/><xs:attribute name="max" type="xs:integer"/><xs:attribute name="includeJson" type="xs:boolean"/></xs:complexType></xs:element><xs:element name="ListMetadataSchemasResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="schema" type="MetadataSchemaDescription"/></xs:sequence><xs:attribute name="offset" type="xs:int"/><xs:attribute name="max" type="xs:int"/><xs:attribute name="totalRecords" type="xs:int"/></xs:complexType></xs:element><xs:element name="DeleteMetadataSchemaRequest"><xs:complexType><xs:sequence><xs:element name="name" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteMetadataSchemaResponse"><xs:complexType><xs:sequence><xs:element name="name" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="SetDefaultMetadataSchemaRequest"><xs:complexType><xs:sequence><xs:element minOccurs="0" name="name" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="SetDefaultMetadataSchemaResponse"><xs:complexType><xs:sequence><xs:element name="name" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="ListProductMetadataSchemasRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence/><xs:attribute name="includeJson" type="xs:boolean"/></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListProductMetadataSchemasResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="schema" type="ProductMetadataSchemaDescription"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="DeleteProductMetadataSchemaRequest"><xs:complexType><xs:sequence><xs:element name="name" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteProductMetadataSchemaResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="ReadOrderMetadataRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadOrderMetadataResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element minOccurs="0" name="payload" type="ns2:PayloadType"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadOrderSectionMetadataRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadOrderSectionMetadataResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="sectionId" type="xs:long"/><xs:element minOccurs="0" name="payload" type="ns2:PayloadType"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateOrderSectionMetadataRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/><xs:element name="payload" type="ns2:PayloadType"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateOrderSectionMetadataResponse"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateOrderMetadataRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="payload" type="ns2:PayloadType"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateOrderMetadataResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="AppCodeValidatorRequest"><xs:complexType><xs:sequence><xs:element name="channelId" type="xs:int"/><xs:element name="code" type="xs:string"/><xs:element minOccurs="0" name="authentication"><xs:complexType><xs:sequence><xs:element name="username" type="xs:string"/><xs:element name="password" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="location"><xs:complexType><xs:attribute name="lat" type="xs:decimal" use="required"/><xs:attribute name="lon" type="xs:decimal" use="required"/></xs:complexType></xs:element><xs:element minOccurs="0" name="locale" type="xs:string"/><xs:element minOccurs="0" name="phonenumber" type="xs:string"/><xs:element minOccurs="0" name="email" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="AppCodeValidatorResponse"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="valid" type="xs:boolean"/><xs:element name="message" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="CodeValidatorRequest"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="entryType" type="EntryChannelType"/><xs:element name="entryAlias" type="xs:string"/><xs:element name="entryId" type="xs:string"/><xs:element minOccurs="0" name="email" type="xs:string"/><xs:element minOccurs="0" name="phonenumber" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="CodeValidatorResponse"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="valid" type="xs:boolean"/><xs:element minOccurs="0" name="validationCount" type="xs:int"/><xs:element minOccurs="0" name="maxValidationCount" type="xs:int"/><xs:element minOccurs="0" name="product" type="Product"/><xs:element name="response" type="xs:string"/><xs:element name="organization" type="ns1:SummaryOrganization"/></xs:sequence></xs:complexType></xs:element><xs:element name="BatchCodeValidatorRequest"><xs:complexType><xs:sequence><xs:element name="codes" type="xs:string"/></xs:sequence><xs:attribute name="returnValid" type="xs:boolean"/><xs:attribute name="returnInvalid" type="xs:boolean"/></xs:complexType></xs:element><xs:element name="BatchCodeValidatorResponse"><xs:complexType><xs:sequence><xs:element name="invalid"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="code"><xs:complexType><xs:simpleContent><xs:extension base="xs:string"/></xs:simpleContent></xs:complexType></xs:element></xs:sequence><xs:attribute form="qualified" name="count" type="xs:integer" use="required"/></xs:complexType></xs:element><xs:element name="valid"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="code"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element minOccurs="0" name="atis"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="ati"><xs:complexType><xs:sequence><xs:element name="web" type="xs:string"/><xs:element name="sms" type="xs:string"/></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element></xs:sequence><xs:attribute form="qualified" name="count" type="xs:integer" use="required"/></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="GetCodeRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="codeIndex" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetCodeResponse"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="CodeDissectorRequest"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="CodeDissectorResponse"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="valid" type="xs:boolean"/><xs:element minOccurs="0" name="orderId" type="xs:long"/><xs:element minOccurs="0" name="orderType" type="xs:string"/><xs:element minOccurs="0" name="owner" type="ns1:SummarySid
2000
"/><xs:element minOccurs="0" name="codeIndex" type="xs:long"/><xs:element minOccurs="0" name="sectionId" type="xs:long"/><xs:element minOccurs="0" name="sectionStart" type="xs:long"/><xs:element minOccurs="0" name="sectionEnd" type="xs:long"/><xs:element minOccurs="0" name="validated" type="xs:int"/><xs:element minOccurs="0" name="maxValidations" type="xs:int"/><xs:element minOccurs="0" name="details" type="xs:string"/><xs:element minOccurs="0" name="external" type="xs:boolean"/><xs:element minOccurs="0" name="pattern" type="xs:string"/><xs:element minOccurs="0" name="prefix" type="xs:string"/><xs:element minOccurs="0" name="length" type="xs:int"/><xs:element minOccurs="0" name="product" type="Product"/><xs:choice><xs:element minOccurs="0" name="hasShadow"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="index" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="isShadow"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="index" type="xs:long"/></xs:sequence></xs:complexType></xs:element></xs:choice><xs:element minOccurs="0" name="sscc" type="xs:string"/><xs:element minOccurs="0" name="statuses"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="status" type="CodeStatus"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="organization" type="xs:string"/><xs:element name="channels"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="channel" type="EntryChannelSummary"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="codeCfg" type="SimpleCodeConfigSummary"/></xs:sequence></xs:complexType></xs:element><xs:element name="CustomerCodeDissectorRequest"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element minOccurs="0" name="cfgId" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element name="CustomerCodeDissectorResponse"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element minOccurs="0" name="orderId" type="xs:long"/><xs:element minOccurs="0" name="codeIndex" type="xs:long"/><xs:element minOccurs="0" name="sectionId" type="xs:long"/><xs:element minOccurs="0" name="section" type="Section"/></xs:sequence></xs:complexType></xs:element><xs:element name="CodeBlacklistRequest"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="CodeBlacklistResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="code" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="CodeBlacklistAddRequest"><xs:complexType><xs:sequence><xs:element name="codes" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="CodeBlacklistAddResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="CodeBlacklistRemoveRequest"><xs:complexType><xs:sequence><xs:element name="codes" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="CodeBlacklistRemoveResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="ValidationsLogFilterRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element minOccurs="0" name="organizationId" type="xs:int"/><xs:element minOccurs="0" name="hideValid" type="xs:boolean"/><xs:element minOccurs="0" name="hideInvalid" type="xs:boolean"/><xs:element minOccurs="0" name="hideVerified" type="xs:boolean"/><xs:element minOccurs="0" name="occurredAfter" type="xs:dateTime"/><xs:element minOccurs="0" name="occurredBefore" type="xs:dateTime"/><xs:element minOccurs="0" name="codes"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="code" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="codeSimilarity" type="xs:float"/><xs:element minOccurs="0" name="ignoreCodeCase" type="xs:boolean"/><xs:element minOccurs="0" name="ips"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="ip" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="phoneNumbers"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="phoneNumber" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="orderIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="sectionIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="productIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="productId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="validationCount" type="ValidationCount"/><xs:element minOccurs="0" name="channelIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="channelId" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="validationType" type="ValidationType"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ValidationsLogFilterResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="entryElement" type="ValidationLogEntry"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="BatchValidationDetailsRequest"><xs:complexType><xs:sequence><xs:element name="batchId" type="xs:string"/></xs:sequence><xs:attribute name="offset" type="xs:long"/><xs:attribute name="max" type="xs:positiveInteger"/></xs:complexType></xs:element><xs:element name="BatchValidationDetailsResponse"><xs:complexType><xs:sequence><xs:element name="batchId" type="xs:string"/><xs:element name="user" type="ns1:OutputUser"/><xs:element name="occurred" type="xs:dateTime"/><xs:element name="valid" type="xs:long"/><xs:element name="verified" type="xs:long"/><xs:element name="invalid" type="xs:long"/><xs:element name="entries"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="entry" type="BatchValidationEntry"/></xs:sequence></xs:complexType></xs:element></xs:sequence><xs:attribute name="offset" type="xs:long"/><xs:attribute name="max" type="xs:positiveInteger"/></xs:complexType></xs:element><xs:element name="BatchValidationsLogRequest"><xs:complexType><xs:attribute name="offset" type="xs:long" use="required"/><xs:attribute name="max" type="xs:positiveInteger" use="required"/><xs:attribute name="occurredAfter" type="xs:dateTime" use="optional"/><xs:attribute name="occurredBefore" type="xs:dateTime" use="optional"/></xs:complexType></xs:element><xs:element name="BatchValidationsLogResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="entryElement"><xs:complexType><xs:sequence><xs:element minOccurs="0" name="batchId" type="xs:string"/><xs:element name="user" type="ns1:OutputUser"/><xs:element name="occurred" type="xs:dateTime"/><xs:element name="valid" type="xs:long"/><xs:element name="verified" type="xs:long"/><xs:element name="invalid" type="xs:long"/></xs:sequence></xs:complexType></xs:element></xs:sequence><xs:attribute name="hasMore" type="xs:boolean" use="required"/></xs:complexType></xs:element><xs:element name="IPLocalizationRequest"><xs:complexType><xs:sequence><xs:element name="ip" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="IPLocalizationResponse"><xs:complexType><xs:sequence><xs:element name="ip" type="xs:string"/><xs:element name="hostname" type="xs:string"/><xs:element name="countryCode" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="StatisticsRequest"><xs:complexType><xs:attribute name="organizationId" type="xs:int" use="optional"/><xs:attribute name
2000
="startTime" type="xs:dateTime" use="optional"/><xs:attribute name="endTime" type="xs:dateTime" use="optional"/></xs:complexType></xs:element><xs:element name="StatisticsResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="entry" type="stat"/></xs:sequence></xs:complexType></xs:element><xs:element name="StatisticsLastOrdersRequest"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="StatisticsLastOrdersResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="order" type="Order"/></xs:sequence></xs:complexType></xs:element><xs:element name="StatisticsLastOrderedExpansionsRequest"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="StatisticsLastOrderedExpansionsResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="expansion" type="OrderExpansionWithOwner"/></xs:sequence></xs:complexType></xs:element><xs:element name="StatisticsLastProducedExpansionsRequest"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="StatisticsLastProducedExpansionsResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="expansion" type="OrderExpansionWithOwner"/></xs:sequence></xs:complexType></xs:element><xs:complexType name="OrderExpansionWithOwner"><xs:complexContent><xs:extension base="OrderExpansion"><xs:sequence><xs:element name="owner" type="ns1:SummarySid"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType><xs:complexType name="stat"><xs:sequence><xs:element name="orders" type="xs:long"/><xs:element name="expansions" type="xs:long"/><xs:element name="codes" type="xs:long"/><xs:element name="invalid" type="xs:long"/><xs:element name="verified" type="xs:long"/><xs:element name="valid" type="xs:long"/></xs:sequence><xs:attribute name="period" type="xs:string" use="required"/></xs:complexType><xs:complexType name="EntryChannel"><xs:sequence><xs:element minOccurs="0" name="id" type="xs:int"/><xs:element minOccurs="0" name="invalidMessage" type="xs:string"/><xs:element name="translations" type="EntryChannelTranslations"/><xs:element maxOccurs="unbounded" minOccurs="0" name="owner"><xs:complexType><xs:choice><xs:element name="organization" type="ns1:Organization"/><xs:element name="organizationId" type="xs:int"/></xs:choice></xs:complexType></xs:element><xs:element minOccurs="0" name="codeConfig"><xs:complexType><xs:sequence><xs:element name="id" type="xs:int"/></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:complexType><xs:complexType name="EntryChannelTranslations"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="translation"><xs:complexType><xs:sequence><xs:element name="country" type="xs:string"/><xs:element name="invalidMessage" type="xs:string"/></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:complexType><xs:complexType name="WebEntryChannel"><xs:complexContent><xs:extension base="EntryChannel"><xs:sequence><xs:element name="alias" type="xs:string"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType><xs:complexType name="SmsEntryChannel"><xs:complexContent><xs:extension base="EntryChannel"><xs:sequence><xs:element name="phonenumber" type="xs:string"/><xs:element minOccurs="0" name="prefix" type="xs:string"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType><xs:element name="CreateEntryChannelRequest"><xs:complexType><xs:sequence><xs:choice><xs:element name="webEntryChannel" type="WebEntryChannel"/><xs:element name="smsEntryChannel" type="SmsEntryChannel"/></xs:choice></xs:sequence></xs:complexType></xs:element><xs:element name="CreateEntryChannelResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateEntryChannelRequest"><xs:complexType><xs:sequence><xs:choice><xs:element name="webEntryChannel" type="WebEntryChannel"/><xs:element name="smsEntryChannel" type="SmsEntryChannel"/></xs:choice></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateEntryChannelResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateEntryChannelTranslationsRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:int"/><xs:element minOccurs="0" name="invalidMessage" type="xs:string"/><xs:element name="translations" type="EntryChannelTranslations"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateEntryChannelTranslationsResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="GetEntryChannelRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetEntryChannelResponse"><xs:complexType><xs:sequence><xs:choice><xs:element name="webEntryChannel" type="WebEntryChannel"/><xs:element name="smsEntryChannel" type="SmsEntryChannel"/></xs:choice></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteEntryChannelRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteEntryChannelResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="ListEntryChannelsRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence/></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListEntryChannelsResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element name="entryChannels"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="entryChannel" type="EntryChannel"/></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="DiskUsageRequest"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="DiskUsageResponse"><xs:complexType><xs:sequence><xs:element name="path" type="xs:string"/><xs:element name="totalDiskSpace" type="xs:long"/><xs:element name="availableDiskSpace" type="xs:long"/><xs:element name="kcengineFilesCount" type="xs:long"/><xs:element name="kcengineFilesSize" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="WorkersInfoRequest"/><xs:element name="WorkersInfoResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="worker" type="worker"/></xs:sequence><xs:attribute name="awaitingProduction" type="xs:long" use="required"/><xs:attribute name="productionRate" type="xs:double" use="required"/><xs:attribute name="productionSpeed" type="xs:double" use="required"/><xs:attribute name="workerThreads" type="xs:long" use="required"/></xs:complexType></xs:element><xs:element name="ExpansionsInfoRequest"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="ExpansionsInfoResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="queuedExpansion" type="queuedExpansion"/><xs:element maxOccurs="unbounded" minOccurs="0" name="strayExpansion" type="strayExpansion"/></xs:sequence></xs:complexType></xs:element><xs:complexType name="queuedExpansion"><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="sequenceNumber" type="xs:long"/><xs:element name="codeCount" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="strayExpansion"><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="sequenceNumber" type="xs:long"/><xs:element name="codeCount" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="worker"><xs:sequence><xs:element name="name" type="xs:string"/><xs:element name="threads" type="xs:long"/><xs:element name="productionRate" type="xs:double"/></xs:sequence></xs:complexType><xs:complexType name="CodeStatusCount"><xs:attribute name="id" type="xs:int"/><xs:attribute name="name" type="xs:string"/><xs:attribute name="count" type="xs:int"/></xs:complexType><xs:complexType name="CodeStatusDelta"><xs:sequence><xs:el
2000
ement maxOccurs="unbounded" minOccurs="0" name="delta"><xs:complexType><xs:sequence><xs:element name="changed"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codestatus" type="CodeStatusCount"/></xs:sequence></xs:complexType></xs:element><xs:element name="skipped"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codestatus" type="CodeStatusCount"/></xs:sequence></xs:complexType></xs:element></xs:sequence><xs:attribute name="orderId" type="xs:long" use="required"/></xs:complexType></xs:element></xs:sequence></xs:complexType><xs:element name="UpdateCodeStatusConfigRequest"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codeStatusField" type="CodeStatusField"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateCodeStatusConfigResponse"><xs:complexType/></xs:element><xs:element name="ReadCodeStatusConfigRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:integer"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadCodeStatusConfigResponse"><xs:complexType><xs:sequence><xs:element name="codeStatusField" type="CodeStatusField"/></xs:sequence></xs:complexType></xs:element><xs:element name="AddCodeStatusConfigRequest"><xs:complexType><xs:sequence><xs:element name="codeStatusField" type="CodeStatusField"/></xs:sequence></xs:complexType></xs:element><xs:element name="AddCodeStatusConfigResponse"><xs:complexType/></xs:element><xs:element name="GetCodeStatusConfigRequest"><xs:complexType/></xs:element><xs:element name="GetCodeStatusConfigResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codeStatusField" type="CodeStatusField"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetCodeStatusHistoryRequest"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetCodeStatusHistoryResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codeStatusSet"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codeStatuses" type="CodeStatus"/></xs:sequence><xs:attribute name="timestamp" type="xs:dateTime"/></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="GetCodeStatusChangesRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element name="from" type="xs:dateTime"/><xs:element minOccurs="0" name="to" type="xs:dateTime"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="GetCodeStatusChangesResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codeStatusSet" type="CodeStatusSnapshot"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:complexType name="AnyOrderCodeStatus"><xs:sequence><xs:element name="statuses"><xs:simpleType><xs:list itemType="xs:int"/></xs:simpleType></xs:element><xs:element name="codes"><xs:simpleType><xs:list itemType="xs:string"/></xs:simpleType></xs:element></xs:sequence><xs:attribute default="true" name="ignoreInvalidCodes" type="xs:boolean"/></xs:complexType><xs:complexType name="CodeStatusResult"><xs:sequence><xs:element name="delta" type="CodeStatusDelta"/><xs:element name="invalidCodes"><xs:simpleType><xs:list itemType="xs:string"/></xs:simpleType></xs:element></xs:sequence><xs:attribute name="additionalPairedCodes" type="xs:int"/></xs:complexType><xs:element name="SetCodeStatusRequest" type="AnyOrderCodeStatus"/><xs:element name="SetCodeStatusResponse" type="CodeStatusResult"/><xs:element name="SetCodeStatusForOrderRequest"><xs:complexType><xs:complexContent><xs:extension base="AnyOrderCodeStatus"><xs:attribute name="orderId" type="xs:long" use="required"/><xs:attribute name="applyToRemaining" type="xs:boolean"/></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="SetCodeStatusForOrderResponse" type="CodeStatusResult"/></xs:schema>
    <schema xmlns="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://kezzlerssp.com/schemas/security" attributeFormDefault="unqualified" elementFormDefault="qualified" targetNamespace="http://kezzlerssp.com/schemas/security"><complexType name="Authentication"><sequence><element minOccurs="0" name="ip" type="string"/><element name="username" type="string"/><element name="time" type="dateTime"/><element minOccurs="0" name="userAgent" type="string"/></sequence><attribute name="eventType" type="string" use="required"/></complexType><complexType name="Organization"><sequence><element minOccurs="0" name="id" type="int"/><element name="name" type="string"/><element name="email" type="string"/><element minOccurs="0" name="adminUser" type="string"/><element minOccurs="0" name="gs1Prefix" type="string"/></sequence></complexType><complexType name="GroupCreate"><sequence><element name="name" type="string"/><element minOccurs="0" name="parentId" type="int"/><element name="roles"><complexType><sequence><element maxOccurs="unbounded" minOccurs="0" name="role" type="tns:GrantedAuthority"/></sequence></complexType></element></sequence><attribute name="representation" type="string" use="optional"/></complexType><complexType name="GroupUpdate"><complexContent><extension base="tns:GroupCreate"><sequence><element minOccurs="0" name="id" type="int"/></sequence></extension></complexContent></complexType><complexType name="Group"><complexContent><extension base="tns:GroupUpdate"><sequence><element name="organization"><complexType><sequence><element name="name" type="string"/></sequence><attribute name="id" type="int" use="required"/></complexType></element></sequence></extension></complexContent></complexType><complexType name="GrantedAuthority"><simpleContent><extension base="string"><attribute name="implicit" type="boolean"/></extension></simpleContent></complexType><complexType name="User"><sequence><element minOccurs="0" name="id" type="int"/><element name="username" type="string"/><element name="email" type="string"/><element minOccurs="0" name="organizationId" type="int"/><element name="enabled" type="boolean"/><element name="credentialsExpired" type="boolean"/><element name="locked" type="boolean"/><element name="defaultGroup"><complexType><sequence><element name="id" type="int"/><element name="name" type="string"/></sequence></complexType></element><element minOccurs="0" name="phoneNumbers"><complexType><sequence><element maxOccurs="unbounded" minOccurs="0" name="phoneNumber" type="string"/></sequence></complexType></element></sequence></complexType><complexType name="InputUser"><sequence><element minOccurs="0" name="id" type="int"/><element name="username" type="string"/><element name="email" type="string"/><element name="enabled" type="boolean"/><element name="locked" type="boolean"/><element name="defaultGroupId" type="int"/><element minOccurs="0" name="plainPassword" type="string"/><element minOccurs="0" name="phoneNumbers"><complexType><sequence><element maxOccurs="unbounded" minOccurs="0" name="phoneNumber" type="string"/></sequence></complexType></element></sequence></complexType><complexType name="OutputUser"><sequence><element minOccurs="0" name="id" type="int"/><element name="username" type="string"/><element name="email" type="string"/><element name="organization" type="tns:Organization"/></sequence></complexType><complexType name="InputUserCertificateMapping"><sequence><element name="certificate" type="tns:InputUserCertificate"/></sequence></complexType><complexType name="OuputUserCertificateMapping"><sequence><element name="user" type="tns:OutputUser"/><element name="certificate" type="tns:InputUserCertificate"/></sequence><attribute name="active" type="boolean" use="required"/></complexType><complexType name="InputUserCertificate"><sequence><element name="issuerCN" type="string"/><element name="certSerial" type="integer"/></sequence></complexType><complexType name="UserPreferences"><sequence><choice><element name="userId" type="int"/><element name="userName" type="stri
2000
ng"/></choice><element name="timezone" type="string"/></sequence></complexType><complexType abstract="true" name="AbstractPermission"><sequence><element name="permissions"><complexType><attribute name="read" type="boolean"/><attribute name="update" type="boolean"/><attribute name="delete" type="boolean"/><attribute name="admin" type="boolean"/></complexType></element></sequence><attribute default="true" name="isGranting" type="boolean"/><attribute name="isOwner" type="boolean"/></complexType><complexType name="ReadPermission"><complexContent><extension base="tns:AbstractPermission"><sequence><element name="sid" type="tns:Sid"/></sequence></extension></complexContent></complexType><complexType name="PermissionResponse"><sequence><element name="object" type="tns:ObjectId"/><element name="aces"><complexType><sequence><element maxOccurs="unbounded" minOccurs="0" name="ace" type="tns:ReadPermission"/></sequence></complexType></element></sequence></complexType><complexType name="CreatePermission"><complexContent><extension base="tns:AbstractPermission"><sequence><element name="sid"><complexType><sequence><choice><element name="userId" type="int"/><element name="groupId" type="int"/><element name="organizationId" type="int"/></choice></sequence></complexType></element></sequence></extension></complexContent></complexType><complexType name="ObjectId"><sequence><element name="id" type="long"/><element name="type" type="string"/></sequence></complexType><complexType name="Sid"><sequence><choice><element name="user" type="tns:User"/><element name="group" type="tns:Group"/><element name="organization" type="tns:Organization"/></choice></sequence></complexType><complexType name="SummaryOrganization"><sequence><element name="id" type="int"/><element name="name" type="string"/></sequence></complexType><complexType name="SummaryGroup"><sequence><element name="id" type="int"/><element name="name" type="string"/><element name="organizationId" type="int"/></sequence></complexType><complexType name="SummaryUser"><sequence><element name="id" type="int"/><element name="username" type="string"/><element name="organizationId" type="int"/><element name="organizationName" type="string"/></sequence></complexType><complexType name="SummarySid"><sequence><choice><element name="user" type="tns:SummaryUser"/><element name="group" type="tns:SummaryGroup"/><element name="organization" type="tns:SummaryOrganization"/></choice></sequence></complexType><complexType name="IpBan"><sequence><element name="ip" type="string"/><element name="issued" type="dateTime"/><element name="expires" type="dateTime"/><element name="reason" type="string"/></sequence></complexType></schema>
    <schema xmlns="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://kezzlerssp.com/schemas/common" attributeFormDefault="unqualified" elementFormDefault="qualified" targetNamespace="http://kezzlerssp.com/schemas/common"><complexType abstract="true" name="PageRequest"><sequence><element minOccurs="0" name="sorting"><complexType><sequence><element maxOccurs="unbounded" minOccurs="0" name="sortBy"><complexType><simpleContent><extension base="string"><attribute name="asc" type="boolean"/></extension></simpleContent></complexType></element></sequence></complexType></element></sequence><attribute default="0" name="offset" type="nonNegativeInteger"><annotation><documentation>The offset in result set</documentation></annotation></attribute><attribute default="25" name="max"><annotation><documentation>The maximum number of results to return in the result set</documentation></annotation><simpleType><restriction base="integer"><maxInclusive value="20000"/></restriction></simpleType></attribute></complexType><complexType abstract="true" name="PageResponse"><sequence/><attribute name="offset" type="int" use="required"><annotation><documentation>The offset used when fetching this result set</documentation></annotation></attribute><attribute name="max" type="int" use="required"><annotation><documentation>The maximum number of results allowed according to the request</documentation></annotation></attribute><attribute name="hasMore" type="boolean" use="required"><annotation><documentation>True if there are more results available</documentation></annotation></attribute><attribute name="totalRecords" type="long" use="optional"><annotation><documentation>The number of items available in total
....</documentation></annotation></attribute></complexType><complexType name="ThreeDimension"><sequence><element name="length" type="decimal"/><element name="height" type="decimal"/><element name="width" type="decimal"/></sequence></complexType><simpleType name="SortOrder"><restriction base="string"><enumeration value="ASC"/><enumeration value="DESC"/></restriction></simpleType><complexType name="QueuedJobType"><sequence><element name="jobId" type="string"/><element name="jobType" type="string"/><element name="created" type="dateTime"/><element minOccurs="0" name="started" type="dateTime"/><element minOccurs="0" name="completed" type="dateTime"/><element minOccurs="0" name="resourceUrl" type="anyURI"/><element minOccurs="0" name="returnUrl" type="anyURI"/><element minOccurs="0" name="result"><complexType><choice><element name="success"><complexType><sequence/></complexType></element><element name="failure"><complexType><sequence><element minOccurs="0" name="errorCode" type="string"/><element name="errorMessage" type="string"/></sequence></complexType></element></choice></complexType></element><element name="progressInfo"><complexType><sequence><element name="stages"><complexType><sequence><element maxOccurs="unbounded" name="stage"><complexType><simpleContent><extension base="string"><attribute name="active" type="boolean"/><attribute name="progress" type="double"/></extension></simpleContent></complexType></element></sequence></complexType></element></sequence></complexType></element><element minOccurs="0" name="extra"><complexType><sequence><element maxOccurs="unbounded" name="entry"><complexType><sequence><element name="name" type="string"/><element name="value" type="string"/></sequence></complexType></element></sequence></complexType></element></sequence></complexType></schema>
    <xs:schema xmlns="http://example.com/fns" xmlns:tns="http://kezzlerssp.com/schema/metadata/foreign/" xmlns:xs="http://www.w3.org/2001/XMLSchema" attributeFormDefault="unqualified" elementFormDefault="qualified" targetNamespace="http://kezzlerssp.com/schema/metadata/foreign/"><xs:complexType name="PayloadType"><xs:sequence><xs:choice maxOccurs="unbounded"><xs:any namespace="##other" processContents="skip"/><xs:any namespace="##local" processContents="skip"/></xs:choice></xs:sequence></xs:complexType></xs:schema>
  </wsdl:types>
  <wsdl:message name="ApplyAtiTemplateGroupRequest">
    <wsdl:part element="tns:ApplyAtiTemplateGroupRequest" name="ApplyAtiTemplateGroupRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateEntryChannelResponse">
    <wsdl:part element="tns:CreateEntryChannelResponse" name="CreateEntryChannelResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadCodeConfigResponse">
    <wsdl:part element="tns:ReadCodeConfigResponse" name="ReadCodeConfigResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListSectionsRequest">
    <wsdl:part element="tns:ListSectionsRequest" name="ListSectionsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetOrderSectionsValidationsResponse">
    <wsdl:part element="tns:GetOrderSectionsValidationsResponse" name="GetOrderSectionsValidationsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ActivateRollSectionResponse">
    <wsdl:part element="tns:ActivateRollSectionResponse" name="ActivateRollSectionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateProductResponse">
    <wsdl:part element="tns:CreateProductResponse" name="CreateProductResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadCodeConfigRequest">
    <wsdl:part element="tns:ReadCodeConfigRequest" name="ReadCodeConfigRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodeRequest">
    <wsdl:part element=
2000
"tns:GetCodeRequest" name="GetCodeRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadSsccResponse">
    <wsdl:part element="tns:ReadSsccResponse" name="ReadSsccResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="MultiExpandOrderResponse">
    <wsdl:part element="tns:MultiExpandOrderResponse" name="MultiExpandOrderResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadAtiResponse">
    <wsdl:part element="tns:ReadAtiResponse" name="ReadAtiResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeBlacklistAddResponse">
    <wsdl:part element="tns:CodeBlacklistAddResponse" name="CodeBlacklistAddResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadCodeStatusConfigRequest">
    <wsdl:part element="tns:ReadCodeStatusConfigRequest" name="ReadCodeStatusConfigRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListExpansionCodesResponse">
    <wsdl:part element="tns:ListExpansionCodesResponse" name="ListExpansionCodesResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListAtisResponse">
    <wsdl:part element="tns:ListAtisResponse" name="ListAtisResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListAtiGroupsRequest">
    <wsdl:part element="tns:ListAtiGroupsRequest" name="ListAtiGroupsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateAtiGroupResponse">
    <wsdl:part element="tns:UpdateAtiGroupResponse" name="UpdateAtiGroupResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ExpandOrderResponse">
    <wsdl:part element="tns:ExpandOrderResponse" name="ExpandOrderResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodesProducedByGroupRequest">
    <wsdl:part element="tns:GetCodesProducedByGroupRequest" name="GetCodesProducedByGroupRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodesProducedByGroupResponse">
    <wsdl:part element="tns:GetCodesProducedByGroupResponse" name="GetCodesProducedByGroupResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="BatchValidationsLogResponse">
    <wsdl:part element="tns:BatchValidationsLogResponse" name="BatchValidationsLogResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ApplyAtiTemplateGroupResponse">
    <wsdl:part element="tns:ApplyAtiTemplateGroupResponse" name="ApplyAtiTemplateGroupResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AddAtiGroupRequest">
    <wsdl:part element="tns:AddAtiGroupRequest" name="AddAtiGroupRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="SetCodeStatusResponse">
    <wsdl:part element="tns:SetCodeStatusResponse" name="SetCodeStatusResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DiskUsageRequest">
    <wsdl:part element="tns:DiskUsageRequest" name="DiskUsageRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeBlacklistRequest">
    <wsdl:part element="tns:CodeBlacklistRequest" name="CodeBlacklistRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListOrdersRequest">
    <wsdl:part element="tns:ListOrdersRequest" name="ListOrdersRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListAllExpansionsResponse">
    <wsdl:part element="tns:ListAllExpansionsResponse" name="ListAllExpansionsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateCodeStatusConfigResponse">
    <wsdl:part element="tns:UpdateCodeStatusConfigResponse" name="UpdateCodeStatusConfigResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateEntryChannelTranslationsResponse">
    <wsdl:part element="tns:UpdateEntryChannelTranslationsResponse" name="UpdateEntryChannelTranslationsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="WorkersInfoRequest">
    <wsdl:part element="tns:WorkersInfoRequest" name="WorkersInfoRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="StatisticsLastOrderedExpansionsResponse">
    <wsdl:part element="tns:StatisticsLastOrderedExpansionsResponse" name="StatisticsLastOrderedExpansionsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodeStatusConfigRequest">
    <wsdl:part element="tns:GetCodeStatusConfigRequest" name="GetCodeStatusConfigRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteProductMetadataSchemaRequest">
    <wsdl:part element="tns:DeleteProductMetadataSchemaRequest" name="DeleteProductMetadataSchemaRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="SetDefaultMetadataSchemaRequest">
    <wsdl:part element="tns:SetDefaultMetadataSchemaRequest" name="SetDefaultMetadataSchemaRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteLastExpansionRequest">
    <wsdl:part element="tns:DeleteLastExpansionRequest" name="DeleteLastExpansionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListOrdersResponse">
    <wsdl:part element="tns:ListOrdersResponse" name="ListOrdersResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CalibrateRollResponse">
    <wsdl:part element="tns:CalibrateRollResponse" name="CalibrateRollResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetOrderValidationsResponse">
    <wsdl:part element="tns:GetOrderValidationsResponse" name="GetOrderValidationsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadSectionRequest">
    <wsdl:part element="tns:ReadSectionRequest" name="ReadSectionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetEntryChannelRequest">
    <wsdl:part element="tns:GetEntryChannelRequest" name="GetEntryChannelRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DefaultAtiGroupRequest">
    <wsdl:part element="tns:DefaultAtiGroupRequest" name="DefaultAtiGroupRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateSectionRequest">
    <wsdl:part element="tns:CreateSectionRequest" name="CreateSectionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AddAtiRequest">
    <wsdl:part element="tns:AddAtiRequest" name="AddAtiRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteReservedSsccSequenceResponse">
    <wsdl:part element="tns:DeleteReservedSsccSequenceResponse" name="DeleteReservedSsccSequenceResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AddReservedSsccSequenceResponse">
    <wsdl:part element="tns:AddReservedSsccSequenceResponse" name="AddReservedSsccSequenceResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListProductsResponse">
    <wsdl:part element="tns:ListProductsResponse" name="ListProductsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AddCodeStatusConfigResponse">
    <wsdl:part element="tns:AddCodeStatusConfigResponse" name="AddCodeStatusConfigResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="StatisticsLastOrdersRequest">
    <wsdl:part element="tns:StatisticsLastOrdersRequest" name="StatisticsLastOrdersRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="FindLookAlikeCodeRequest">
    <wsdl:part element="tns:FindLookAlikeCodeRequest" name="FindLookAlikeCodeRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="SetExpansionStatusResponse">
    <wsdl:part element="tns:SetExpansionStatusResponse" name="SetExpansionStatusResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateProductResponse">
    <wsdl:part element="tns:UpdateProductResponse" name="UpdateProductResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetOrderExpansionsValidationsResponse">
    <wsdl:part element="tns:GetOrderExpansionsValidationsResponse" name="GetOrderExpansionsValidationsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListSectionAtisRequest">
    <wsdl:part element="tns:ListSectionAtisRequest" name="ListSectionAtisRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="StatisticsLastProducedExpansionsResponse">
    <wsdl:part element="tns:StatisticsLastProducedExpansionsResponse" name="StatisticsLastProducedExpansionsResponse">
    </wsdl:part>
  </wsdl:mess
2000
age>
  <wsdl:message name="DeleteLastExpansionResponse">
    <wsdl:part element="tns:DeleteLastExpansionResponse" name="DeleteLastExpansionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UnlinkAtiRequest">
    <wsdl:part element="tns:UnlinkAtiRequest" name="UnlinkAtiRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListCodeConfigsRequest">
    <wsdl:part element="tns:ListCodeConfigsRequest" name="ListCodeConfigsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeactivateSectionRequest">
    <wsdl:part element="tns:DeactivateSectionRequest" name="DeactivateSectionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UnlinkAllAtisRequest">
    <wsdl:part element="tns:UnlinkAllAtisRequest" name="UnlinkAllAtisRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeActivateSectionInRollRequest">
    <wsdl:part element="tns:DeActivateSectionInRollRequest" name="DeActivateSectionInRollRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetOrderCodeStatusStatisticsResponse">
    <wsdl:part element="tns:GetOrderCodeStatusStatisticsResponse" name="GetOrderCodeStatusStatisticsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DownloadCodesRequest">
    <wsdl:part element="tns:DownloadCodesRequest" name="DownloadCodesRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetProductRequest">
    <wsdl:part element="tns:GetProductRequest" name="GetProductRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListCodePatternsRequest">
    <wsdl:part element="tns:ListCodePatternsRequest" name="ListCodePatternsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListSectionsResponse">
    <wsdl:part element="tns:ListSectionsResponse" name="ListSectionsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AddAtiGroupResponse">
    <wsdl:part element="tns:AddAtiGroupResponse" name="AddAtiGroupResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateNewSectionInRollResponse">
    <wsdl:part element="tns:CreateNewSectionInRollResponse" name="CreateNewSectionInRollResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UnlinkAllAtisResponse">
    <wsdl:part element="tns:UnlinkAllAtisResponse" name="UnlinkAllAtisResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodesProducedByProductRequest">
    <wsdl:part element="tns:GetCodesProducedByProductRequest" name="GetCodesProducedByProductRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListAtiGroupsResponse">
    <wsdl:part element="tns:ListAtiGroupsResponse" name="ListAtiGroupsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ValidationsLogFilterRequest">
    <wsdl:part element="tns:ValidationsLogFilterRequest" name="ValidationsLogFilterRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateOrderSectionMetadataResponse">
    <wsdl:part element="tns:UpdateOrderSectionMetadataResponse" name="UpdateOrderSectionMetadataResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetOrderValidationsRequest">
    <wsdl:part element="tns:GetOrderValidationsRequest" name="GetOrderValidationsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteEntryChannelRequest">
    <wsdl:part element="tns:DeleteEntryChannelRequest" name="DeleteEntryChannelRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeActivateSectionInRollResponse">
    <wsdl:part element="tns:DeActivateSectionInRollResponse" name="DeActivateSectionInRollResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateOrderMetadataRequest">
    <wsdl:part element="tns:UpdateOrderMetadataRequest" name="UpdateOrderMetadataRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="WorkersInfoResponse">
    <wsdl:part element="tns:WorkersInfoResponse" name="WorkersInfoResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListAllExpansionsRequest">
    <wsdl:part element="tns:ListAllExpansionsRequest" name="ListAllExpansionsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="BatchValidationsLogRequest">
    <wsdl:part element="tns:BatchValidationsLogRequest" name="BatchValidationsLogRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteProductMetadataSchemaResponse">
    <wsdl:part element="tns:DeleteProductMetadataSchemaResponse" name="DeleteProductMetadataSchemaResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetOrderCodeStatusStatisticsRequest">
    <wsdl:part element="tns:GetOrderCodeStatusStatisticsRequest" name="GetOrderCodeStatusStatisticsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodesProducedByUserResponse">
    <wsdl:part element="tns:GetCodesProducedByUserResponse" name="GetCodesProducedByUserResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodeStatusChangesRequest">
    <wsdl:part element="tns:GetCodeStatusChangesRequest" name="GetCodeStatusChangesRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateAtiRequest">
    <wsdl:part element="tns:UpdateAtiRequest" name="UpdateAtiRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListAtisRequest">
    <wsdl:part element="tns:ListAtisRequest" name="ListAtisRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListProductsRequest">
    <wsdl:part element="tns:ListProductsRequest" name="ListProductsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateCodeStatusConfigRequest">
    <wsdl:part element="tns:UpdateCodeStatusConfigRequest" name="UpdateCodeStatusConfigRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeValidatorResponse">
    <wsdl:part element="tns:CodeValidatorResponse" name="CodeValidatorResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeDissectorResponse">
    <wsdl:part element="tns:CodeDissectorResponse" name="CodeDissectorResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AppCodeValidatorResponse">
    <wsdl:part element="tns:AppCodeValidatorResponse" name="AppCodeValidatorResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CustomerCodeDissectorRequest">
    <wsdl:part element="tns:CustomerCodeDissectorRequest" name="CustomerCodeDissectorRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetRollResponse">
    <wsdl:part element="tns:GetRollResponse" name="GetRollResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="SetCodeStatusForOrderRequest">
    <wsdl:part element="tns:SetCodeStatusForOrderRequest" name="SetCodeStatusForOrderRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ApplyAtiGroupResponse">
    <wsdl:part element="tns:ApplyAtiGroupResponse" name="ApplyAtiGroupResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeactivateSectionResponse">
    <wsdl:part element="tns:DeactivateSectionResponse" name="DeactivateSectionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeValidatorRequest">
    <wsdl:part element="tns:CodeValidatorRequest" name="CodeValidatorRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="LockOrderRequest">
    <wsdl:part element="tns:LockOrderRequest" name="LockOrderRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateEntryChannelRequest">
    <wsdl:part element="tns:UpdateEntryChannelRequest" name="UpdateEntryChannelRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AddAtiResponse">
    <wsdl:part element="tns:AddAtiResponse" name="AddAtiResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="StatisticsResponse">
    <wsdl:part element="tns:StatisticsResponse" name="StatisticsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="FindLookAlikeCodeResponse">
    <wsdl:part element="tns:FindLookAlikeCodeResponse" name="FindLookAlikeCodeResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="IPLocalizationResponse">
    <wsdl:part element="tns:IPLocalizationResponse" name="IPLocalizationResponse">
    </wsdl:part>
  </wsdl:message>

2000
  <wsdl:message name="ExpansionsStatusRequest">
    <wsdl:part element="tns:ExpansionsStatusRequest" name="ExpansionsStatusRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeBlacklistRemoveRequest">
    <wsdl:part element="tns:CodeBlacklistRemoveRequest" name="CodeBlacklistRemoveRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodesProducedByProductResponse">
    <wsdl:part element="tns:GetCodesProducedByProductResponse" name="GetCodesProducedByProductResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeBlacklistResponse">
    <wsdl:part element="tns:CodeBlacklistResponse" name="CodeBlacklistResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="SetCodeStatusForOrderResponse">
    <wsdl:part element="tns:SetCodeStatusForOrderResponse" name="SetCodeStatusForOrderResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteMetadataSchemaRequest">
    <wsdl:part element="tns:DeleteMetadataSchemaRequest" name="DeleteMetadataSchemaRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteOrderSectionMetadataResponse">
    <wsdl:part element="tns:DeleteOrderSectionMetadataResponse" name="DeleteOrderSectionMetadataResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ExpansionsInfoRequest">
    <wsdl:part element="tns:ExpansionsInfoRequest" name="ExpansionsInfoRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListExpansionsRequest">
    <wsdl:part element="tns:ListExpansionsRequest" name="ListExpansionsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadRollResponse">
    <wsdl:part element="tns:ReadRollResponse" name="ReadRollResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodeStatusHistoryRequest">
    <wsdl:part element="tns:GetCodeStatusHistoryRequest" name="GetCodeStatusHistoryRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeBlacklistAddRequest">
    <wsdl:part element="tns:CodeBlacklistAddRequest" name="CodeBlacklistAddRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateSectionResponse">
    <wsdl:part element="tns:UpdateSectionResponse" name="UpdateSectionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="SetCodeStatusRequest">
    <wsdl:part element="tns:SetCodeStatusRequest" name="SetCodeStatusRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateProductRequest">
    <wsdl:part element="tns:CreateProductRequest" name="CreateProductRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateAtiGroupRequest">
    <wsdl:part element="tns:UpdateAtiGroupRequest" name="UpdateAtiGroupRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ActivateRollSectionRequest">
    <wsdl:part element="tns:ActivateRollSectionRequest" name="ActivateRollSectionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateOrderDataRequest">
    <wsdl:part element="tns:UpdateOrderDataRequest" name="UpdateOrderDataRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ExpandOrderRequest">
    <wsdl:part element="tns:ExpandOrderRequest" name="ExpandOrderRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="RenameAtiRequest">
    <wsdl:part element="tns:RenameAtiRequest" name="RenameAtiRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateCodeConfigRequest">
    <wsdl:part element="tns:CreateCodeConfigRequest" name="CreateCodeConfigRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="StatisticsLastOrderedExpansionsRequest">
    <wsdl:part element="tns:StatisticsLastOrderedExpansionsRequest" name="StatisticsLastOrderedExpansionsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListEntryChannelsRequest">
    <wsdl:part element="tns:ListEntryChannelsRequest" name="ListEntryChannelsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetProductResponse">
    <wsdl:part element="tns:GetProductResponse" name="GetProductResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ApplyAtiRequest">
    <wsdl:part element="tns:ApplyAtiRequest" name="ApplyAtiRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="SetDefaultMetadataSchemaResponse">
    <wsdl:part element="tns:SetDefaultMetadataSchemaResponse" name="SetDefaultMetadataSchemaResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadOrderRequest">
    <wsdl:part element="tns:ReadOrderRequest" name="ReadOrderRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="RenameAtiResponse">
    <wsdl:part element="tns:RenameAtiResponse" name="RenameAtiResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DefaultAtiGroupResponse">
    <wsdl:part element="tns:DefaultAtiGroupResponse" name="DefaultAtiGroupResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetExpansionResponse">
    <wsdl:part element="tns:GetExpansionResponse" name="GetExpansionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeBlacklistRemoveResponse">
    <wsdl:part element="tns:CodeBlacklistRemoveResponse" name="CodeBlacklistRemoveResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateOrderResponse">
    <wsdl:part element="tns:UpdateOrderResponse" name="UpdateOrderResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteAtiRequest">
    <wsdl:part element="tns:DeleteAtiRequest" name="DeleteAtiRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateEntryChannelRequest">
    <wsdl:part element="tns:CreateEntryChannelRequest" name="CreateEntryChannelRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateOrderMetadataResponse">
    <wsdl:part element="tns:UpdateOrderMetadataResponse" name="UpdateOrderMetadataResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ApplyAtiResponse">
    <wsdl:part element="tns:ApplyAtiResponse" name="ApplyAtiResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="MapExpansionsToSectionsResponse">
    <wsdl:part element="tns:MapExpansionsToSectionsResponse" name="MapExpansionsToSectionsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CalibrateRollRequest">
    <wsdl:part element="tns:CalibrateRollRequest" name="CalibrateRollRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadAtiRequest">
    <wsdl:part element="tns:ReadAtiRequest" name="ReadAtiRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateCodeConfigResponse">
    <wsdl:part element="tns:CreateCodeConfigResponse" name="CreateCodeConfigResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadAtiGroupRequest">
    <wsdl:part element="tns:ReadAtiGroupRequest" name="ReadAtiGroupRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateOrderSectionMetadataRequest">
    <wsdl:part element="tns:UpdateOrderSectionMetadataRequest" name="UpdateOrderSectionMetadataRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="BatchCodeValidatorRequest">
    <wsdl:part element="tns:BatchCodeValidatorRequest" name="BatchCodeValidatorRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="IPLocalizationRequest">
    <wsdl:part element="tns:IPLocalizationRequest" name="IPLocalizationRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DownloadCodesResponse">
    <wsdl:part element="tns:DownloadCodesResponse" name="DownloadCodesResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="BatchCodeValidatorResponse">
    <wsdl:part element="tns:BatchCodeValidatorResponse" name="BatchCodeValidatorResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="StatisticsRequest">
    <wsdl:part element="tns:StatisticsRequest" name="StatisticsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteMetadataSchemaResponse">
    <wsdl:part element="tns:DeleteMetadataSchemaResponse" name="DeleteMetadataSchemaResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadRollRequest">
    <wsdl:part element="tns:ReadRollRequest" name="ReadRollRequest">
    </wsdl:part>
  </wsdl:messa
2000
ge>
  <wsdl:message name="InitOrderRequest">
    <wsdl:part element="tns:InitOrderRequest" name="InitOrderRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateSsccSequenceResponse">
    <wsdl:part element="tns:CreateSsccSequenceResponse" name="CreateSsccSequenceResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteSectionRequest">
    <wsdl:part element="tns:DeleteSectionRequest" name="DeleteSectionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="StatisticsLastProducedExpansionsRequest">
    <wsdl:part element="tns:StatisticsLastProducedExpansionsRequest" name="StatisticsLastProducedExpansionsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UnlinkAtiResponse">
    <wsdl:part element="tns:UnlinkAtiResponse" name="UnlinkAtiResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListCodePatternsResponse">
    <wsdl:part element="tns:ListCodePatternsResponse" name="ListCodePatternsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadSsccSequenceRequest">
    <wsdl:part element="tns:ReadSsccSequenceRequest" name="ReadSsccSequenceRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetExpansionRequest">
    <wsdl:part element="tns:GetExpansionRequest" name="GetExpansionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateEntryChannelTranslationsRequest">
    <wsdl:part element="tns:UpdateEntryChannelTranslationsRequest" name="UpdateEntryChannelTranslationsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateOrderRequest">
    <wsdl:part element="tns:UpdateOrderRequest" name="UpdateOrderRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="InitOrderResponse">
    <wsdl:part element="tns:InitOrderResponse" name="InitOrderResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="MapExpansionsToSectionsRequest">
    <wsdl:part element="tns:MapExpansionsToSectionsRequest" name="MapExpansionsToSectionsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetOrderExpansionsValidationsRequest">
    <wsdl:part element="tns:GetOrderExpansionsValidationsRequest" name="GetOrderExpansionsValidationsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="IdentifyRollRequest">
    <wsdl:part element="tns:IdentifyRollRequest" name="IdentifyRollRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AddCodeStatusConfigRequest">
    <wsdl:part element="tns:AddCodeStatusConfigRequest" name="AddCodeStatusConfigRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteAtiGroupRequest">
    <wsdl:part element="tns:DeleteAtiGroupRequest" name="DeleteAtiGroupRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ApplyAtiGroupRequest">
    <wsdl:part element="tns:ApplyAtiGroupRequest" name="ApplyAtiGroupRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListMetadataSchemasRequest">
    <wsdl:part element="tns:ListMetadataSchemasRequest" name="ListMetadataSchemasRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadCodeStatusConfigResponse">
    <wsdl:part element="tns:ReadCodeStatusConfigResponse" name="ReadCodeStatusConfigResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListReservedSsccSequenceRequest">
    <wsdl:part element="tns:ListReservedSsccSequenceRequest" name="ListReservedSsccSequenceRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateOrderDataResponse">
    <wsdl:part element="tns:UpdateOrderDataResponse" name="UpdateOrderDataResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadOrderSectionMetadataRequest">
    <wsdl:part element="tns:ReadOrderSectionMetadataRequest" name="ReadOrderSectionMetadataRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListMetadataSchemasResponse">
    <wsdl:part element="tns:ListMetadataSchemasResponse" name="ListMetadataSchemasResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadOrderResponse">
    <wsdl:part element="tns:ReadOrderResponse" name="ReadOrderResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="LockOrderResponse">
    <wsdl:part element="tns:LockOrderResponse" name="LockOrderResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="IdentifyRollResponse">
    <wsdl:part element="tns:IdentifyRollResponse" name="IdentifyRollResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListCodeConfigsResponse">
    <wsdl:part element="tns:ListCodeConfigsResponse" name="ListCodeConfigsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadOrderSectionMetadataResponse">
    <wsdl:part element="tns:ReadOrderSectionMetadataResponse" name="ReadOrderSectionMetadataResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetOrderSectionsValidationsRequest">
    <wsdl:part element="tns:GetOrderSectionsValidationsRequest" name="GetOrderSectionsValidationsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListProductMetadataSchemasRequest">
    <wsdl:part element="tns:ListProductMetadataSchemasRequest" name="ListProductMetadataSchemasRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="StatisticsLastOrdersResponse">
    <wsdl:part element="tns:StatisticsLastOrdersResponse" name="StatisticsLastOrdersResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListSectionAtisResponse">
    <wsdl:part element="tns:ListSectionAtisResponse" name="ListSectionAtisResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListEntryChannelsResponse">
    <wsdl:part element="tns:ListEntryChannelsResponse" name="ListEntryChannelsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ExpansionsStatusResponse">
    <wsdl:part element="tns:ExpansionsStatusResponse" name="ExpansionsStatusResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="BatchValidationDetailsRequest">
    <wsdl:part element="tns:BatchValidationDetailsRequest" name="BatchValidationDetailsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateAtiResponse">
    <wsdl:part element="tns:UpdateAtiResponse" name="UpdateAtiResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListProductMetadataSchemasResponse">
    <wsdl:part element="tns:ListProductMetadataSchemasResponse" name="ListProductMetadataSchemasResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="MarkTemporaryRollEndRequest">
    <wsdl:part element="tns:MarkTemporaryRollEndRequest" name="MarkTemporaryRollEndRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteSectionResponse">
    <wsdl:part element="tns:DeleteSectionResponse" name="DeleteSectionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodeStatusChangesResponse">
    <wsdl:part element="tns:GetCodeStatusChangesResponse" name="GetCodeStatusChangesResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteOrderMetadataResponse">
    <wsdl:part element="tns:DeleteOrderMetadataResponse" name="DeleteOrderMetadataResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListExpansionsResponse">
    <wsdl:part element="tns:ListExpansionsResponse" name="ListExpansionsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeDissectorRequest">
    <wsdl:part element="tns:CodeDissectorRequest" name="CodeDissectorRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateSsccSequenceRequest">
    <wsdl:part element="tns:CreateSsccSequenceRequest" name="CreateSsccSequenceRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadSsccRequest">
    <wsdl:part element="tns:ReadSsccRequest" name="ReadSsccRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateProductRequest">
    <wsdl:part element="tns:UpdateProductRequest" name="UpdateProductRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadAtiGroupResponse">
    <wsdl:part element="tns:ReadAtiGroupResponse" name="ReadAtiGroupResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DiskUsageResponse">
    <wsdl:part element="tns:
2000
DiskUsageResponse" name="DiskUsageResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetRollRequest">
    <wsdl:part element="tns:GetRollRequest" name="GetRollRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AddReservedSsccSequenceRequest">
    <wsdl:part element="tns:AddReservedSsccSequenceRequest" name="AddReservedSsccSequenceRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListExpansionCodesRequest">
    <wsdl:part element="tns:ListExpansionCodesRequest" name="ListExpansionCodesRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AppCodeValidatorRequest">
    <wsdl:part element="tns:AppCodeValidatorRequest" name="AppCodeValidatorRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodeResponse">
    <wsdl:part element="tns:GetCodeResponse" name="GetCodeResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateSectionResponse">
    <wsdl:part element="tns:CreateSectionResponse" name="CreateSectionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteAtiResponse">
    <wsdl:part element="tns:DeleteAtiResponse" name="DeleteAtiResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListReservedSsccSequenceResponse">
    <wsdl:part element="tns:ListReservedSsccSequenceResponse" name="ListReservedSsccSequenceResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteProductResponse">
    <wsdl:part element="tns:DeleteProductResponse" name="DeleteProductResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateSectionRequest">
    <wsdl:part element="tns:UpdateSectionRequest" name="UpdateSectionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadOrderMetadataRequest">
    <wsdl:part element="tns:ReadOrderMetadataRequest" name="ReadOrderMetadataRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodesProducedByUserRequest">
    <wsdl:part element="tns:GetCodesProducedByUserRequest" name="GetCodesProducedByUserRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteOrderMetadataRequest">
    <wsdl:part element="tns:DeleteOrderMetadataRequest" name="DeleteOrderMetadataRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ActivateSectionResponse">
    <wsdl:part element="tns:ActivateSectionResponse" name="ActivateSectionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="MarkTemporaryRollEndResponse">
    <wsdl:part element="tns:MarkTemporaryRollEndResponse" name="MarkTemporaryRollEndResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadOrderMetadataResponse">
    <wsdl:part element="tns:ReadOrderMetadataResponse" name="ReadOrderMetadataResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CustomerCodeDissectorResponse">
    <wsdl:part element="tns:CustomerCodeDissectorResponse" name="CustomerCodeDissectorResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ValidationsLogFilterResponse">
    <wsdl:part element="tns:ValidationsLogFilterResponse" name="ValidationsLogFilterResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetEntryChannelResponse">
    <wsdl:part element="tns:GetEntryChannelResponse" name="GetEntryChannelResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateNewSectionInRollRequest">
    <wsdl:part element="tns:CreateNewSectionInRollRequest" name="CreateNewSectionInRollRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="SetExpansionStatusRequest">
    <wsdl:part element="tns:SetExpansionStatusRequest" name="SetExpansionStatusRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteReservedSsccSequenceRequest">
    <wsdl:part element="tns:DeleteReservedSsccSequenceRequest" name="DeleteReservedSsccSequenceRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteEntryChannelResponse">
    <wsdl:part element="tns:DeleteEntryChannelResponse" name="DeleteEntryChannelResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodeStatusConfigResponse">
    <wsdl:part element="tns:GetCodeStatusConfigResponse" name="GetCodeStatusConfigResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadSectionResponse">
    <wsdl:part element="tns:ReadSectionResponse" name="ReadSectionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodeStatusHistoryResponse">
    <wsdl:part element="tns:GetCodeStatusHistoryResponse" name="GetCodeStatusHistoryResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteAtiGroupResponse">
    <wsdl:part element="tns:DeleteAtiGroupResponse" name="DeleteAtiGroupResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="BatchValidationDetailsResponse">
    <wsdl:part element="tns:BatchValidationDetailsResponse" name="BatchValidationDetailsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteOrderSectionMetadataRequest">
    <wsdl:part element="tns:DeleteOrderSectionMetadataRequest" name="DeleteOrderSectionMetadataRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadSsccSequenceResponse">
    <wsdl:part element="tns:ReadSsccSequenceResponse" name="ReadSsccSequenceResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ExpansionsInfoResponse">
    <wsdl:part element="tns:ExpansionsInfoResponse" name="ExpansionsInfoResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="MultiExpandOrderRequest">
    <wsdl:part element="tns:MultiExpandOrderRequest" name="MultiExpandOrderRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ActivateSectionRequest">
    <wsdl:part element="tns:ActivateSectionRequest" name="ActivateSectionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteProductRequest">
    <wsdl:part element="tns:DeleteProductRequest" name="DeleteProductRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateEntryChannelResponse">
    <wsdl:part element="tns:UpdateEntryChannelResponse" name="UpdateEntryChannelResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:portType name="kcengine">
    <wsdl:operation name="ApplyAtiTemplateGroup">
      <wsdl:input message="tns:ApplyAtiTemplateGroupRequest" name="ApplyAtiTemplateGroupRequest">
    </wsdl:input>
      <wsdl:output message="tns:ApplyAtiTemplateGroupResponse" name="ApplyAtiTemplateGroupResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateEntryChannel">
      <wsdl:input message="tns:CreateEntryChannelRequest" name="CreateEntryChannelRequest">
    </wsdl:input>
      <wsdl:output message="tns:CreateEntryChannelResponse" name="CreateEntryChannelResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadCodeConfig">
      <wsdl:input message="tns:ReadCodeConfigRequest" name="ReadCodeConfigRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadCodeConfigResponse" name="ReadCodeConfigResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListSections">
      <wsdl:input message="tns:ListSectionsRequest" name="ListSectionsRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListSectionsResponse" name="ListSectionsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetOrderSectionsValidations">
      <wsdl:input message="tns:GetOrderSectionsValidationsRequest" name="GetOrderSectionsValidationsRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetOrderSectionsValidationsResponse" name="GetOrderSectionsValidationsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ActivateRollSection">
      <wsdl:input message="tns:ActivateRollSectionRequest" name="ActivateRollSectionRequest">
    </wsdl:input>
      <wsdl:output message="tns:ActivateRollSectionResponse" name="ActivateRollSectionResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateProduct">
      <wsdl:input message="tns:CreateProductRequest" name="CreateProductRequest">
    </wsdl:input>
      <wsdl:output message="tns:CreateProductResponse" name="CreateProductResponse">
    </wsdl:output>
    </ws
2000
dl:operation>
    <wsdl:operation name="GetCode">
      <wsdl:input message="tns:GetCodeRequest" name="GetCodeRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetCodeResponse" name="GetCodeResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadSscc">
      <wsdl:input message="tns:ReadSsccRequest" name="ReadSsccRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadSsccResponse" name="ReadSsccResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="MultiExpandOrder">
      <wsdl:input message="tns:MultiExpandOrderRequest" name="MultiExpandOrderRequest">
    </wsdl:input>
      <wsdl:output message="tns:MultiExpandOrderResponse" name="MultiExpandOrderResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadAti">
      <wsdl:input message="tns:ReadAtiRequest" name="ReadAtiRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadAtiResponse" name="ReadAtiResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeBlacklistAdd">
      <wsdl:input message="tns:CodeBlacklistAddRequest" name="CodeBlacklistAddRequest">
    </wsdl:input>
      <wsdl:output message="tns:CodeBlacklistAddResponse" name="CodeBlacklistAddResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadCodeStatusConfig">
      <wsdl:input message="tns:ReadCodeStatusConfigRequest" name="ReadCodeStatusConfigRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadCodeStatusConfigResponse" name="ReadCodeStatusConfigResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListExpansionCodes">
      <wsdl:input message="tns:ListExpansionCodesRequest" name="ListExpansionCodesRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListExpansionCodesResponse" name="ListExpansionCodesResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListAtis">
      <wsdl:input message="tns:ListAtisRequest" name="ListAtisRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListAtisResponse" name="ListAtisResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListAtiGroups">
      <wsdl:input message="tns:ListAtiGroupsRequest" name="ListAtiGroupsRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListAtiGroupsResponse" name="ListAtiGroupsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateAtiGroup">
      <wsdl:input message="tns:UpdateAtiGroupRequest" name="UpdateAtiGroupRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateAtiGroupResponse" name="UpdateAtiGroupResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ExpandOrder">
      <wsdl:input message="tns:ExpandOrderRequest" name="ExpandOrderRequest">
    </wsdl:input>
      <wsdl:output message="tns:ExpandOrderResponse" name="ExpandOrderResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodesProducedByGroup">
      <wsdl:input message="tns:GetCodesProducedByGroupRequest" name="GetCodesProducedByGroupRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetCodesProducedByGroupResponse" name="GetCodesProducedByGroupResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="BatchValidationsLog">
      <wsdl:input message="tns:BatchValidationsLogRequest" name="BatchValidationsLogRequest">
    </wsdl:input>
      <wsdl:output message="tns:BatchValidationsLogResponse" name="BatchValidationsLogResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AddAtiGroup">
      <wsdl:input message="tns:AddAtiGroupRequest" name="AddAtiGroupRequest">
    </wsdl:input>
      <wsdl:output message="tns:AddAtiGroupResponse" name="AddAtiGroupResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="SetCodeStatus">
      <wsdl:input message="tns:SetCodeStatusRequest" name="SetCodeStatusRequest">
    </wsdl:input>
      <wsdl:output message="tns:SetCodeStatusResponse" name="SetCodeStatusResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DiskUsage">
      <wsdl:input message="tns:DiskUsageRequest" name="DiskUsageRequest">
    </wsdl:input>
      <wsdl:output message="tns:DiskUsageResponse" name="DiskUsageResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeBlacklist">
      <wsdl:input message="tns:CodeBlacklistRequest" name="CodeBlacklistRequest">
    </wsdl:input>
      <wsdl:output message="tns:CodeBlacklistResponse" name="CodeBlacklistResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListOrders">
      <wsdl:input message="tns:ListOrdersRequest" name="ListOrdersRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListOrdersResponse" name="ListOrdersResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListAllExpansions">
      <wsdl:input message="tns:ListAllExpansionsRequest" name="ListAllExpansionsRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListAllExpansionsResponse" name="ListAllExpansionsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateCodeStatusConfig">
      <wsdl:input message="tns:UpdateCodeStatusConfigRequest" name="UpdateCodeStatusConfigRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateCodeStatusConfigResponse" name="UpdateCodeStatusConfigResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateEntryChannelTranslations">
      <wsdl:input message="tns:UpdateEntryChannelTranslationsRequest" name="UpdateEntryChannelTranslationsRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateEntryChannelTranslationsResponse" name="UpdateEntryChannelTranslationsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="WorkersInfo">
      <wsdl:input message="tns:WorkersInfoRequest" name="WorkersInfoRequest">
    </wsdl:input>
      <wsdl:output message="tns:WorkersInfoResponse" name="WorkersInfoResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="StatisticsLastOrderedExpansions">
      <wsdl:input message="tns:StatisticsLastOrderedExpansionsRequest" name="StatisticsLastOrderedExpansionsRequest">
    </wsdl:input>
      <wsdl:output message="tns:StatisticsLastOrderedExpansionsResponse" name="StatisticsLastOrderedExpansionsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodeStatusConfig">
      <wsdl:input message="tns:GetCodeStatusConfigRequest" name="GetCodeStatusConfigRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetCodeStatusConfigResponse" name="GetCodeStatusConfigResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteProductMetadataSchema">
      <wsdl:input message="tns:DeleteProductMetadataSchemaRequest" name="DeleteProductMetadataSchemaRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteProductMetadataSchemaResponse" name="DeleteProductMetadataSchemaResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="SetDefaultMetadataSchema">
      <wsdl:input message="tns:SetDefaultMetadataSchemaRequest" name="SetDefaultMetadataSchemaRequest">
    </wsdl:input>
      <wsdl:output message="tns:SetDefaultMetadataSchemaResponse" name="SetDefaultMetadataSchemaResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteLastExpansion">
      <wsdl:input message="tns:DeleteLastExpansionRequest" name="DeleteLastExpansionRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteLastExpansionResponse" name="DeleteLastExpansionResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CalibrateRoll">
      <wsdl:input message="tns:CalibrateRollRequest" name="CalibrateRollRequest">
    </wsdl:input>
      <wsdl:output message="tns:CalibrateRollResponse" name="CalibrateRollResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetOrderValidations">
      <wsdl:input message="tns:GetOrderValidationsRequest" name="GetOrderValidationsRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetOrderValidationsResponse" name="GetOrderValidationsRes
2000
ponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadSection">
      <wsdl:input message="tns:ReadSectionRequest" name="ReadSectionRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadSectionResponse" name="ReadSectionResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetEntryChannel">
      <wsdl:input message="tns:GetEntryChannelRequest" name="GetEntryChannelRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetEntryChannelResponse" name="GetEntryChannelResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DefaultAtiGroup">
      <wsdl:input message="tns:DefaultAtiGroupRequest" name="DefaultAtiGroupRequest">
    </wsdl:input>
      <wsdl:output message="tns:DefaultAtiGroupResponse" name="DefaultAtiGroupResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateSection">
      <wsdl:input message="tns:CreateSectionRequest" name="CreateSectionRequest">
    </wsdl:input>
      <wsdl:output message="tns:CreateSectionResponse" name="CreateSectionResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AddAti">
      <wsdl:input message="tns:AddAtiRequest" name="AddAtiRequest">
    </wsdl:input>
      <wsdl:output message="tns:AddAtiResponse" name="AddAtiResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteReservedSsccSequence">
      <wsdl:input message="tns:DeleteReservedSsccSequenceRequest" name="DeleteReservedSsccSequenceRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteReservedSsccSequenceResponse" name="DeleteReservedSsccSequenceResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AddReservedSsccSequence">
      <wsdl:input message="tns:AddReservedSsccSequenceRequest" name="AddReservedSsccSequenceRequest">
    </wsdl:input>
      <wsdl:output message="tns:AddReservedSsccSequenceResponse" name="AddReservedSsccSequenceResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListProducts">
      <wsdl:input message="tns:ListProductsRequest" name="ListProductsRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListProductsResponse" name="ListProductsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AddCodeStatusConfig">
      <wsdl:input message="tns:AddCodeStatusConfigRequest" name="AddCodeStatusConfigRequest">
    </wsdl:input>
      <wsdl:output message="tns:AddCodeStatusConfigResponse" name="AddCodeStatusConfigResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="StatisticsLastOrders">
      <wsdl:input message="tns:StatisticsLastOrdersRequest" name="StatisticsLastOrdersRequest">
    </wsdl:input>
      <wsdl:output message="tns:StatisticsLastOrdersResponse" name="StatisticsLastOrdersResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="FindLookAlikeCode">
      <wsdl:input message="tns:FindLookAlikeCodeRequest" name="FindLookAlikeCodeRequest">
    </wsdl:input>
      <wsdl:output message="tns:FindLookAlikeCodeResponse" name="FindLookAlikeCodeResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="SetExpansionStatus">
      <wsdl:input message="tns:SetExpansionStatusRequest" name="SetExpansionStatusRequest">
    </wsdl:input>
      <wsdl:output message="tns:SetExpansionStatusResponse" name="SetExpansionStatusResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateProduct">
      <wsdl:input message="tns:UpdateProductRequest" name="UpdateProductRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateProductResponse" name="UpdateProductResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetOrderExpansionsValidations">
      <wsdl:input message="tns:GetOrderExpansionsValidationsRequest" name="GetOrderExpansionsValidationsRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetOrderExpansionsValidationsResponse" name="GetOrderExpansionsValidationsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListSectionAtis">
      <wsdl:input message="tns:ListSectionAtisRequest" name="ListSectionAtisRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListSectionAtisResponse" name="ListSectionAtisResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="StatisticsLastProducedExpansions">
      <wsdl:input message="tns:StatisticsLastProducedExpansionsRequest" name="StatisticsLastProducedExpansionsRequest">
    </wsdl:input>
      <wsdl:output message="tns:StatisticsLastProducedExpansionsResponse" name="StatisticsLastProducedExpansionsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UnlinkAti">
      <wsdl:input message="tns:UnlinkAtiRequest" name="UnlinkAtiRequest">
    </wsdl:input>
      <wsdl:output message="tns:UnlinkAtiResponse" name="UnlinkAtiResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListCodeConfigs">
      <wsdl:input message="tns:ListCodeConfigsRequest" name="ListCodeConfigsRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListCodeConfigsResponse" name="ListCodeConfigsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeactivateSection">
      <wsdl:input message="tns:DeactivateSectionRequest" name="DeactivateSectionRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeactivateSectionResponse" name="DeactivateSectionResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UnlinkAllAtis">
      <wsdl:input message="tns:UnlinkAllAtisRequest" name="UnlinkAllAtisRequest">
    </wsdl:input>
      <wsdl:output message="tns:UnlinkAllAtisResponse" name="UnlinkAllAtisResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeActivateSectionInRoll">
      <wsdl:input message="tns:DeActivateSectionInRollRequest" name="DeActivateSectionInRollRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeActivateSectionInRollResponse" name="DeActivateSectionInRollResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetOrderCodeStatusStatistics">
      <wsdl:input message="tns:GetOrderCodeStatusStatisticsRequest" name="GetOrderCodeStatusStatisticsRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetOrderCodeStatusStatisticsResponse" name="GetOrderCodeStatusStatisticsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DownloadCodes">
      <wsdl:input message="tns:DownloadCodesRequest" name="DownloadCodesRequest">
    </wsdl:input>
      <wsdl:output message="tns:DownloadCodesResponse" name="DownloadCodesResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetProduct">
      <wsdl:input message="tns:GetProductRequest" name="GetProductRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetProductResponse" name="GetProductResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListCodePatterns">
      <wsdl:input message="tns:ListCodePatternsRequest" name="ListCodePatternsRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListCodePatternsResponse" name="ListCodePatternsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateNewSectionInRoll">
      <wsdl:input message="tns:CreateNewSectionInRollRequest" name="CreateNewSectionInRollRequest">
    </wsdl:input>
      <wsdl:output message="tns:CreateNewSectionInRollResponse" name="CreateNewSectionInRollResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodesProducedByProduct">
      <wsdl:input message="tns:GetCodesProducedByProductRequest" name="GetCodesProducedByProductRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetCodesProducedByProductResponse" name="GetCodesProducedByProductResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ValidationsLogFilter">
      <wsdl:input message="tns:ValidationsLogFilterRequest" name="ValidationsLogFilterRequest">
    </wsdl:input>
      <wsdl:output message="tns:ValidationsLogFilterResponse" name="ValidationsLogFilterResponse">
    </wsdl:output>
    </
2000
wsdl:operation>
    <wsdl:operation name="UpdateOrderSectionMetadata">
      <wsdl:input message="tns:UpdateOrderSectionMetadataRequest" name="UpdateOrderSectionMetadataRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateOrderSectionMetadataResponse" name="UpdateOrderSectionMetadataResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteEntryChannel">
      <wsdl:input message="tns:DeleteEntryChannelRequest" name="DeleteEntryChannelRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteEntryChannelResponse" name="DeleteEntryChannelResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateOrderMetadata">
      <wsdl:input message="tns:UpdateOrderMetadataRequest" name="UpdateOrderMetadataRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateOrderMetadataResponse" name="UpdateOrderMetadataResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodesProducedByUser">
      <wsdl:input message="tns:GetCodesProducedByUserRequest" name="GetCodesProducedByUserRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetCodesProducedByUserResponse" name="GetCodesProducedByUserResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodeStatusChanges">
      <wsdl:input message="tns:GetCodeStatusChangesRequest" name="GetCodeStatusChangesRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetCodeStatusChangesResponse" name="GetCodeStatusChangesResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateAti">
      <wsdl:input message="tns:UpdateAtiRequest" name="UpdateAtiRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateAtiResponse" name="UpdateAtiResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeValidator">
      <wsdl:input message="tns:CodeValidatorRequest" name="CodeValidatorRequest">
    </wsdl:input>
      <wsdl:output message="tns:CodeValidatorResponse" name="CodeValidatorResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeDissector">
      <wsdl:input message="tns:CodeDissectorRequest" name="CodeDissectorRequest">
    </wsdl:input>
      <wsdl:output message="tns:CodeDissectorResponse" name="CodeDissectorResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AppCodeValidator">
      <wsdl:input message="tns:AppCodeValidatorRequest" name="AppCodeValidatorRequest">
    </wsdl:input>
      <wsdl:output message="tns:AppCodeValidatorResponse" name="AppCodeValidatorResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CustomerCodeDissector">
      <wsdl:input message="tns:CustomerCodeDissectorRequest" name="CustomerCodeDissectorRequest">
    </wsdl:input>
      <wsdl:output message="tns:CustomerCodeDissectorResponse" name="CustomerCodeDissectorResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetRoll">
      <wsdl:input message="tns:GetRollRequest" name="GetRollRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetRollResponse" name="GetRollResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="SetCodeStatusForOrder">
      <wsdl:input message="tns:SetCodeStatusForOrderRequest" name="SetCodeStatusForOrderRequest">
    </wsdl:input>
      <wsdl:output message="tns:SetCodeStatusForOrderResponse" name="SetCodeStatusForOrderResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ApplyAtiGroup">
      <wsdl:input message="tns:ApplyAtiGroupRequest" name="ApplyAtiGroupRequest">
    </wsdl:input>
      <wsdl:output message="tns:ApplyAtiGroupResponse" name="ApplyAtiGroupResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="LockOrder">
      <wsdl:input message="tns:LockOrderRequest" name="LockOrderRequest">
    </wsdl:input>
      <wsdl:output message="tns:LockOrderResponse" name="LockOrderResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateEntryChannel">
      <wsdl:input message="tns:UpdateEntryChannelRequest" name="UpdateEntryChannelRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateEntryChannelResponse" name="UpdateEntryChannelResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="Statistics">
      <wsdl:input message="tns:StatisticsRequest" name="StatisticsRequest">
    </wsdl:input>
      <wsdl:output message="tns:StatisticsResponse" name="StatisticsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="IPLocalization">
      <wsdl:input message="tns:IPLocalizationRequest" name="IPLocalizationRequest">
    </wsdl:input>
      <wsdl:output message="tns:IPLocalizationResponse" name="IPLocalizationResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ExpansionsStatus">
      <wsdl:input message="tns:ExpansionsStatusRequest" name="ExpansionsStatusRequest">
    </wsdl:input>
      <wsdl:output message="tns:ExpansionsStatusResponse" name="ExpansionsStatusResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeBlacklistRemove">
      <wsdl:input message="tns:CodeBlacklistRemoveRequest" name="CodeBlacklistRemoveRequest">
    </wsdl:input>
      <wsdl:output message="tns:CodeBlacklistRemoveResponse" name="CodeBlacklistRemoveResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteMetadataSchema">
      <wsdl:input message="tns:DeleteMetadataSchemaRequest" name="DeleteMetadataSchemaRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteMetadataSchemaResponse" name="DeleteMetadataSchemaResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteOrderSectionMetadata">
      <wsdl:input message="tns:DeleteOrderSectionMetadataRequest" name="DeleteOrderSectionMetadataRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteOrderSectionMetadataResponse" name="DeleteOrderSectionMetadataResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ExpansionsInfo">
      <wsdl:input message="tns:ExpansionsInfoRequest" name="ExpansionsInfoRequest">
    </wsdl:input>
      <wsdl:output message="tns:ExpansionsInfoResponse" name="ExpansionsInfoResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListExpansions">
      <wsdl:input message="tns:ListExpansionsRequest" name="ListExpansionsRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListExpansionsResponse" name="ListExpansionsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadRoll">
      <wsdl:input message="tns:ReadRollRequest" name="ReadRollRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadRollResponse" name="ReadRollResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodeStatusHistory">
      <wsdl:input message="tns:GetCodeStatusHistoryRequest" name="GetCodeStatusHistoryRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetCodeStatusHistoryResponse" name="GetCodeStatusHistoryResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateSection">
      <wsdl:input message="tns:UpdateSectionRequest" name="UpdateSectionRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateSectionResponse" name="UpdateSectionResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateOrderData">
      <wsdl:input message="tns:UpdateOrderDataRequest" name="UpdateOrderDataRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateOrderDataResponse" name="UpdateOrderDataResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="RenameAti">
      <wsdl:input message="tns:RenameAtiRequest" name="RenameAtiRequest">
    </wsdl:input>
      <wsdl:output message="tns:RenameAtiResponse" name="RenameAtiResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateCodeConfig">
      <wsdl:input message="tns:CreateCodeConfigRequest" name="CreateCodeConfigRequest">
    </wsdl:input>
      <wsdl:output message="tns:CreateCodeConfigResponse" name="CreateCodeConfigResponse">
    </wsdl:output>
    </wsdl:opera
2000
tion>
    <wsdl:operation name="ListEntryChannels">
      <wsdl:input message="tns:ListEntryChannelsRequest" name="ListEntryChannelsRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListEntryChannelsResponse" name="ListEntryChannelsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ApplyAti">
      <wsdl:input message="tns:ApplyAtiRequest" name="ApplyAtiRequest">
    </wsdl:input>
      <wsdl:output message="tns:ApplyAtiResponse" name="ApplyAtiResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadOrder">
      <wsdl:input message="tns:ReadOrderRequest" name="ReadOrderRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadOrderResponse" name="ReadOrderResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetExpansion">
      <wsdl:input message="tns:GetExpansionRequest" name="GetExpansionRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetExpansionResponse" name="GetExpansionResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateOrder">
      <wsdl:input message="tns:UpdateOrderRequest" name="UpdateOrderRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateOrderResponse" name="UpdateOrderResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteAti">
      <wsdl:input message="tns:DeleteAtiRequest" name="DeleteAtiRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteAtiResponse" name="DeleteAtiResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="MapExpansionsToSections">
      <wsdl:input message="tns:MapExpansionsToSectionsRequest" name="MapExpansionsToSectionsRequest">
    </wsdl:input>
      <wsdl:output message="tns:MapExpansionsToSectionsResponse" name="MapExpansionsToSectionsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadAtiGroup">
      <wsdl:input message="tns:ReadAtiGroupRequest" name="ReadAtiGroupRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadAtiGroupResponse" name="ReadAtiGroupResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="BatchCodeValidator">
      <wsdl:input message="tns:BatchCodeValidatorRequest" name="BatchCodeValidatorRequest">
    </wsdl:input>
      <wsdl:output message="tns:BatchCodeValidatorResponse" name="BatchCodeValidatorResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="InitOrder">
      <wsdl:input message="tns:InitOrderRequest" name="InitOrderRequest">
    </wsdl:input>
      <wsdl:output message="tns:InitOrderResponse" name="InitOrderResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateSsccSequence">
      <wsdl:input message="tns:CreateSsccSequenceRequest" name="CreateSsccSequenceRequest">
    </wsdl:input>
      <wsdl:output message="tns:CreateSsccSequenceResponse" name="CreateSsccSequenceResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteSection">
      <wsdl:input message="tns:DeleteSectionRequest" name="DeleteSectionRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteSectionResponse" name="DeleteSectionResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadSsccSequence">
      <wsdl:input message="tns:ReadSsccSequenceRequest" name="ReadSsccSequenceRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadSsccSequenceResponse" name="ReadSsccSequenceResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="IdentifyRoll">
      <wsdl:input message="tns:IdentifyRollRequest" name="IdentifyRollRequest">
    </wsdl:input>
      <wsdl:output message="tns:IdentifyRollResponse" name="IdentifyRollResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteAtiGroup">
      <wsdl:input message="tns:DeleteAtiGroupRequest" name="DeleteAtiGroupRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteAtiGroupResponse" name="DeleteAtiGroupResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListMetadataSchemas">
      <wsdl:input message="tns:ListMetadataSchemasRequest" name="ListMetadataSchemasRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListMetadataSchemasResponse" name="ListMetadataSchemasResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListReservedSsccSequence">
      <wsdl:input message="tns:ListReservedSsccSequenceRequest" name="ListReservedSsccSequenceRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListReservedSsccSequenceResponse" name="ListReservedSsccSequenceResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadOrderSectionMetadata">
      <wsdl:input message="tns:ReadOrderSectionMetadataRequest" name="ReadOrderSectionMetadataRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadOrderSectionMetadataResponse" name="ReadOrderSectionMetadataResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListProductMetadataSchemas">
      <wsdl:input message="tns:ListProductMetadataSchemasRequest" name="ListProductMetadataSchemasRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListProductMetadataSchemasResponse" name="ListProductMetadataSchemasResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="BatchValidationDetails">
      <wsdl:input message="tns:BatchValidationDetailsRequest" name="BatchValidationDetailsRequest">
    </wsdl:input>
      <wsdl:output message="tns:BatchValidationDetailsResponse" name="BatchValidationDetailsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="MarkTemporaryRollEnd">
      <wsdl:input message="tns:MarkTemporaryRollEndRequest" name="MarkTemporaryRollEndRequest">
    </wsdl:input>
      <wsdl:output message="tns:MarkTemporaryRollEndResponse" name="MarkTemporaryRollEndResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteOrderMetadata">
      <wsdl:input message="tns:DeleteOrderMetadataRequest" name="DeleteOrderMetadataRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteOrderMetadataResponse" name="DeleteOrderMetadataResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteProduct">
      <wsdl:input message="tns:DeleteProductRequest" name="DeleteProductRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteProductResponse" name="DeleteProductResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadOrderMetadata">
      <wsdl:input message="tns:ReadOrderMetadataRequest" name="ReadOrderMetadataRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadOrderMetadataResponse" name="ReadOrderMetadataResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ActivateSection">
      <wsdl:input message="tns:ActivateSectionRequest" name="ActivateSectionRequest">
    </wsdl:input>
      <wsdl:output message="tns:ActivateSectionResponse" name="ActivateSectionResponse">
    </wsdl:output>
    </wsdl:operation>
  </wsdl:portType>
  <wsdl:binding name="kcengineSoap11" type="tns:kcengine">
    <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
    <wsdl:operation name="ApplyAtiTemplateGroup">
      <soap:operation soapAction=""/>
      <wsdl:input name="ApplyAtiTemplateGroupRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ApplyAtiTemplateGroupResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateEntryChannel">
      <soap:operation soapAction=""/>
      <wsdl:input name="CreateEntryChannelRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CreateEntryChannelResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadCodeConfig">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadCodeConfigRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadCodeConfigResponse">
        <soap:body use="literal"/>
      </wsdl:output>

2000
    </wsdl:operation>
    <wsdl:operation name="ListSections">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListSectionsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListSectionsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetOrderSectionsValidations">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetOrderSectionsValidationsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetOrderSectionsValidationsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ActivateRollSection">
      <soap:operation soapAction=""/>
      <wsdl:input name="ActivateRollSectionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ActivateRollSectionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateProduct">
      <soap:operation soapAction=""/>
      <wsdl:input name="CreateProductRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CreateProductResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCode">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetCodeRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetCodeResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadSscc">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadSsccRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadSsccResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="MultiExpandOrder">
      <soap:operation soapAction=""/>
      <wsdl:input name="MultiExpandOrderRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="MultiExpandOrderResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadAti">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadAtiRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadAtiResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeBlacklistAdd">
      <soap:operation soapAction=""/>
      <wsdl:input name="CodeBlacklistAddRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CodeBlacklistAddResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadCodeStatusConfig">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadCodeStatusConfigRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadCodeStatusConfigResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListExpansionCodes">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListExpansionCodesRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListExpansionCodesResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListAtis">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListAtisRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListAtisResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListAtiGroups">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListAtiGroupsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListAtiGroupsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateAtiGroup">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateAtiGroupRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateAtiGroupResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ExpandOrder">
      <soap:operation soapAction=""/>
      <wsdl:input name="ExpandOrderRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ExpandOrderResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodesProducedByGroup">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetCodesProducedByGroupRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetCodesProducedByGroupResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="BatchValidationsLog">
      <soap:operation soapAction=""/>
      <wsdl:input name="BatchValidationsLogRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="BatchValidationsLogResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AddAtiGroup">
      <soap:operation soapAction=""/>
      <wsdl:input name="AddAtiGroupRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="AddAtiGroupResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="SetCodeStatus">
      <soap:operation soapAction=""/>
      <wsdl:input name="SetCodeStatusRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="SetCodeStatusResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DiskUsage">
      <soap:operation soapAction=""/>
      <wsdl:input name="DiskUsageRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DiskUsageResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeBlacklist">
      <soap:operation soapAction=""/>
      <wsdl:input name="CodeBlacklistRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CodeBlacklistResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListOrders">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListOrdersRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListOrdersResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListAllExpansions">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListAllExpansionsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListAllExpansionsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateCodeStatusConfig">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateCodeStatusConfigRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateCodeStatusConfigResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateEntryChannelTranslations">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateEntryChannelTranslationsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateEntryChannelTranslationsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="WorkersInfo">
      <soap:operation soapAction=""/>
      <wsdl:input name="WorkersInfoRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="WorkersInfoResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:
2000
operation>
    <wsdl:operation name="StatisticsLastOrderedExpansions">
      <soap:operation soapAction=""/>
      <wsdl:input name="StatisticsLastOrderedExpansionsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="StatisticsLastOrderedExpansionsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodeStatusConfig">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetCodeStatusConfigRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetCodeStatusConfigResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteProductMetadataSchema">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteProductMetadataSchemaRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteProductMetadataSchemaResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="SetDefaultMetadataSchema">
      <soap:operation soapAction=""/>
      <wsdl:input name="SetDefaultMetadataSchemaRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="SetDefaultMetadataSchemaResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteLastExpansion">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteLastExpansionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteLastExpansionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CalibrateRoll">
      <soap:operation soapAction=""/>
      <wsdl:input name="CalibrateRollRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CalibrateRollResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetOrderValidations">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetOrderValidationsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetOrderValidationsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadSection">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadSectionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadSectionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetEntryChannel">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetEntryChannelRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetEntryChannelResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DefaultAtiGroup">
      <soap:operation soapAction=""/>
      <wsdl:input name="DefaultAtiGroupRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DefaultAtiGroupResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateSection">
      <soap:operation soapAction=""/>
      <wsdl:input name="CreateSectionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CreateSectionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AddAti">
      <soap:operation soapAction=""/>
      <wsdl:input name="AddAtiRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="AddAtiResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteReservedSsccSequence">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteReservedSsccSequenceRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteReservedSsccSequenceResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AddReservedSsccSequence">
      <soap:operation soapAction=""/>
      <wsdl:input name="AddReservedSsccSequenceRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="AddReservedSsccSequenceResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListProducts">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListProductsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListProductsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AddCodeStatusConfig">
      <soap:operation soapAction=""/>
      <wsdl:input name="AddCodeStatusConfigRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="AddCodeStatusConfigResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="StatisticsLastOrders">
      <soap:operation soapAction=""/>
      <wsdl:input name="StatisticsLastOrdersRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="StatisticsLastOrdersResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="FindLookAlikeCode">
      <soap:operation soapAction=""/>
      <wsdl:input name="FindLookAlikeCodeRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="FindLookAlikeCodeResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="SetExpansionStatus">
      <soap:operation soapAction=""/>
      <wsdl:input name="SetExpansionStatusRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="SetExpansionStatusResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateProduct">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateProductRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateProductResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetOrderExpansionsValidations">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetOrderExpansionsValidationsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetOrderExpansionsValidationsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListSectionAtis">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListSectionAtisRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListSectionAtisResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="StatisticsLastProducedExpansions">
      <soap:operation soapAction=""/>
      <wsdl:input name="StatisticsLastProducedExpansionsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="StatisticsLastProducedExpansionsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UnlinkAti">
      <soap:operation soapAction=""/>
      <wsdl:input name="UnlinkAtiRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UnlinkAtiResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListCodeConfigs">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListCodeConfigsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListCodeConfigsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeactivateSection">
     
2000
 <soap:operation soapAction=""/>
      <wsdl:input name="DeactivateSectionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeactivateSectionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UnlinkAllAtis">
      <soap:operation soapAction=""/>
      <wsdl:input name="UnlinkAllAtisRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UnlinkAllAtisResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeActivateSectionInRoll">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeActivateSectionInRollRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeActivateSectionInRollResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetOrderCodeStatusStatistics">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetOrderCodeStatusStatisticsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetOrderCodeStatusStatisticsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DownloadCodes">
      <soap:operation soapAction=""/>
      <wsdl:input name="DownloadCodesRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DownloadCodesResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetProduct">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetProductRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetProductResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListCodePatterns">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListCodePatternsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListCodePatternsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateNewSectionInRoll">
      <soap:operation soapAction=""/>
      <wsdl:input name="CreateNewSectionInRollRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CreateNewSectionInRollResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodesProducedByProduct">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetCodesProducedByProductRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetCodesProducedByProductResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ValidationsLogFilter">
      <soap:operation soapAction=""/>
      <wsdl:input name="ValidationsLogFilterRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ValidationsLogFilterResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateOrderSectionMetadata">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateOrderSectionMetadataRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateOrderSectionMetadataResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteEntryChannel">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteEntryChannelRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteEntryChannelResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateOrderMetadata">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateOrderMetadataRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateOrderMetadataResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodesProducedByUser">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetCodesProducedByUserRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetCodesProducedByUserResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodeStatusChanges">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetCodeStatusChangesRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetCodeStatusChangesResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateAti">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateAtiRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateAtiResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeValidator">
      <soap:operation soapAction=""/>
      <wsdl:input name="CodeValidatorRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CodeValidatorResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeDissector">
      <soap:operation soapAction=""/>
      <wsdl:input name="CodeDissectorRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CodeDissectorResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AppCodeValidator">
      <soap:operation soapAction=""/>
      <wsdl:input name="AppCodeValidatorRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="AppCodeValidatorResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CustomerCodeDissector">
      <soap:operation soapAction=""/>
      <wsdl:input name="CustomerCodeDissectorRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CustomerCodeDissectorResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetRoll">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetRollRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetRollResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="SetCodeStatusForOrder">
      <soap:operation soapAction=""/>
      <wsdl:input name="SetCodeStatusForOrderRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="SetCodeStatusForOrderResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ApplyAtiGroup">
      <soap:operation soapAction=""/>
      <wsdl:input name="ApplyAtiGroupRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ApplyAtiGroupResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="LockOrder">
      <soap:operation soapAction=""/>
      <wsdl:input name="LockOrderRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="LockOrderResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateEntryChannel">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateEntryChannelRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateEntryChannelResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="Statistics">
      <soap:operation soapAction=""/>
      <wsdl:input name="StatisticsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output na
2000
me="StatisticsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="IPLocalization">
      <soap:operation soapAction=""/>
      <wsdl:input name="IPLocalizationRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="IPLocalizationResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ExpansionsStatus">
      <soap:operation soapAction=""/>
      <wsdl:input name="ExpansionsStatusRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ExpansionsStatusResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeBlacklistRemove">
      <soap:operation soapAction=""/>
      <wsdl:input name="CodeBlacklistRemoveRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CodeBlacklistRemoveResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteMetadataSchema">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteMetadataSchemaRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteMetadataSchemaResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteOrderSectionMetadata">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteOrderSectionMetadataRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteOrderSectionMetadataResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ExpansionsInfo">
      <soap:operation soapAction=""/>
      <wsdl:input name="ExpansionsInfoRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ExpansionsInfoResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListExpansions">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListExpansionsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListExpansionsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadRoll">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadRollRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadRollResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodeStatusHistory">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetCodeStatusHistoryRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetCodeStatusHistoryResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateSection">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateSectionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateSectionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateOrderData">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateOrderDataRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateOrderDataResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="RenameAti">
      <soap:operation soapAction=""/>
      <wsdl:input name="RenameAtiRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="RenameAtiResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateCodeConfig">
      <soap:operation soapAction=""/>
      <wsdl:input name="CreateCodeConfigRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CreateCodeConfigResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListEntryChannels">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListEntryChannelsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListEntryChannelsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ApplyAti">
      <soap:operation soapAction=""/>
      <wsdl:input name="ApplyAtiRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ApplyAtiResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadOrder">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadOrderRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadOrderResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetExpansion">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetExpansionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetExpansionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateOrder">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateOrderRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateOrderResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteAti">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteAtiRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteAtiResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="MapExpansionsToSections">
      <soap:operation soapAction=""/>
      <wsdl:input name="MapExpansionsToSectionsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="MapExpansionsToSectionsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadAtiGroup">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadAtiGroupRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadAtiGroupResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="BatchCodeValidator">
      <soap:operation soapAction=""/>
      <wsdl:input name="BatchCodeValidatorRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="BatchCodeValidatorResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="InitOrder">
      <soap:operation soapAction=""/>
      <wsdl:input name="InitOrderRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="InitOrderResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateSsccSequence">
      <soap:operation soapAction=""/>
      <wsdl:input name="CreateSsccSequenceRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CreateSsccSequenceResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteSection">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteSectionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteSectionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadSsccSequence">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadSsccSequenceRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadSsccSequenceResponse">
        <s
1000
oap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="IdentifyRoll">
      <soap:operation soapAction=""/>
      <wsdl:input name="IdentifyRollRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="IdentifyRollResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteAtiGroup">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteAtiGroupRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteAtiGroupResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListMetadataSchemas">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListMetadataSchemasRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListMetadataSchemasResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListReservedSsccSequence">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListReservedSsccSequenceRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListReservedSsccSequenceResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadOrderSectionMetadata">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadOrderSectionMetadataRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadOrderSectionMetadataResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListProductMetadataSchemas">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListProductMetadataSchemasRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListProductMetadataSchemasResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="BatchValidationDetails">
      <soap:operation soapAction=""/>
      <wsdl:input name="BatchValidationDetailsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="BatchValidationDetailsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="MarkTemporaryRollEnd">
      <soap:operation soapAction=""/>
      <wsdl:input name="MarkTemporaryRollEndRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="MarkTemporaryRollEndResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteOrderMetadata">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteOrderMetadataRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteOrderMetadataResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteProduct">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteProductRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteProductResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadOrderMetadata">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadOrderMetadataRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadOrderMetadataResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ActivateSection">
      <soap:operation soapAction=""/>
      <wsdl:input name="ActivateSectionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ActivateSectionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
  </wsdl:binding>
  <wsdl:service name="kcengineService">
    <wsdl:port binding="tns:kcengineSoap11" name="kceng
81
ineSoap11">
      <soap:address location="192.168.0.193/ssp/kcengine-ws"/>
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
0'''

received_wsdl_message = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?><wsdl:definitions xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xmlns:sch0="http://kezzlerssp.com/schemas/kcengine" xmlns:sch1="http://kezzlerssp.com/schemas/security" xmlns:sch2="http://kezzlerssp.com/schemas/common" xmlns:sch3="http://kezzlerssp.com/schema/metadata/foreign/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tns="http://kezzlerssp.com/schemas/kcengine" targetNamespace="http://kezzlerssp.com/schemas/kcengine">
  <wsdl:types>
    <xs:schema xmlns="http://kezzlerssp.com/schemas/kcengine" xmlns:ns0="http://kezzlerssp.com/schemas/common" xmlns:ns1="http://kezzlerssp.com/schemas/security" xmlns:ns2="http://kezzlerssp.com/schema/metadata/foreign/" xmlns:xs="http://www.w3.org/2001/XMLSchema" attributeFormDefault="unqualified" elementFormDefault="qualified" targetNamespace="http://kezzlerssp.com/schemas/kcengine"><xs:import namespace="http://kezzlerssp.com/schemas/common"/><xs:import namespace="http://kezzlerssp.com/schemas/security"/><xs:import namespace="http://kezzlerssp.com/schemas/common"/><xs:import namespace="http://kezzlerssp.com/schemas/common"/><xs:import namespace="http://kezzlerssp.com/schemas/common"/><xs:import namespace="http://kezzlerssp.com/schemas/common"/><xs:import namespace="http://kezzlerssp.com/schema/metadata/foreign/"/><xs:import namespace="http://kezzlerssp.com/schemas/security"/><xs:import namespace="http://kezzlerssp.com/schemas/security"/><xs:import namespace="http://kezzlerssp.com/schemas/common"/><xs:import namespace="http://kezzlerssp.com/schemas/security"/><xs:import namespace="http://kezzlerssp.com/schemas/common"/><xs:import namespace="http://kezzlerssp.com/schemas/security"/><xs:import namespace="http://kezzlerssp.com/schemas/common"/><xs:element name="ListCodePatternsRequest"><xs:annotation><xs:documentation>Request a list of all available code types that can be ordered.</xs:documentation></xs:annotation><xs:complexType/></xs:element><xs:element name="ListCodePatternsResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codePattern"><xs:complexType><xs:attribute name="id" type="xs:string" use="required"><xs:annotation><xs:documentation>The ID of the code pattern</xs:documentation></xs:annotation></xs:attribute><xs:attribute name="description" type="xs:string" use="required"><xs:annotation><xs:documentation>A text description of the code pattern</xs:documentation></xs:annotation></xs:attribute><xs:attribute name="minLength" type="xs:positiveInteger" use="required"><xs:annotation><xs:documentation>The minimum code length that can be ordered</xs:documentation></xs:annotation></xs:attribute><xs:attribute name="defaultLength" type="xs:positiveInteger" use="required"><xs:annotation><xs:documentation>The default code length of this code pattern</xs:documentation></xs:annotation></xs:attribute><xs:attribute name="maxLength" type="xs:positiveInteger" use="required"><xs:annotation><xs:documentation>The maximum code length allowed for this code pattern</xs:documentation></xs:annotation></xs:attribute><xs:attribute name="caseSensitive" type="xs:boolean" use="required"><xs:annotation><xs:documentation>Whether this code is case sensitive or not</xs:documentation></xs:annotation></xs:attribute></xs:complexType></xs:element></xs:sequence><xs:attribute name="defaultCase" type="CodeCase" use="required"><xs:annotation><xs:documentation>The default code case if the code is case-insensitive</xs:documentation></xs:annotation></xs:attribute></xs:complexType></xs:element><xs:element name="ListOrdersRequest"><xs:annotation><xs:documentation>Request a list of all available orders with optional filtering offset and maximum number of results.</xs:documentation></xs:annotation><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element minOccurs="0" name="metadataFilter" type="xs:string"><xs:annotation><xs:documentation>A search string that will filter all orders not containing the meta-data
                                    described in the expression.
                                </xs:documentation></xs:annotation></xs:element><xs:element minOccurs="0" name="descriptionFilter" type="xs:string"><xs:annotation><xs:documentation>A search string that will filter all orders not containing the
                                    description search string
                                </xs:documentation></xs:annotation></xs:element></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListOrdersResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="order" type="Order"><xs:annotation><xs:documentation>Zero or more orders</xs:documentation></xs:annotation></xs:element></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="InitOrderRequest"><xs:annotation><xs:documentation>Create a new empty order containing zero codes. Use [expandOrder] to request codes for the order.</xs:documentation></xs:annotation><xs:complexType><xs:sequence><xs:element minOccurs="0" name="type" type="OrderType"><xs:annotation><xs:documentation>Deprecated! Do not use</xs:documentation></xs:annotation></xs:element><xs:element default="false" minOccurs="0" name="sectioned" type="xs:boolean"><xs:annotation><xs:documentation>Should this order be split into section. Usaually used only with pre-printed media</xs:documentation></xs:annotation></xs:element><xs:element minOccurs="0" name="description" type="xs:string"><xs:annotation><xs:documentation>An optional description of the order</xs:documentation></xs:annotation></xs:element><xs:element minOccurs="0" name="productId" type="xs:int"><xs:annotation><xs:documentation>An optional product ID. Has to match a previously registered product ID, see [listProducts]</xs:documentation></xs:annotation></xs:element><xs:element minOccurs="0" name="gtin" type="xs:string"><xs:annotation><xs:documentation>An optional product GTIN. Has to match a previously registered product's GTIN, see [listProducts]</xs:documentation></xs:annotation></xs:element><xs:element minOccurs="0" name="metadataSchema" type="xs:string"><xs:annotation><xs:documentation>An optional meta-data schema ID. Has to match a previously registered schema ID, see [listMetadataSchemas]</xs:documentation></xs:annotation></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="InitOrderResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"><xs:annotation><xs:documentation>The ID of the created order</xs:documentation></xs:annotation></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateOrderRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element minOccurs="0" name="description" nillable="true" type="xs:string"/><xs:element minOccurs="0" name="productId" nillable="true" type="xs:int"/><xs:element minOccurs="0" name="metadataSchema" nillable="true" type="xs:string"/><xs:element minOccurs="0" name="sectioned" type="xs:boolean"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateOrderResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateOrderDataRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element minOccurs="0" name="description" type="xs:string"/><xs:element minOccurs="0" name="productId" type="xs:int"/><xs:element minOccurs="0" name="metadataSchema" type="xs:string"/><xs:element minOccurs="0" name="sectioned" type="xs:boolean"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateOrderDataResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="LockOrderRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="LockOrderResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadOrderRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadOrderResponse" type="Order"/><xs:element name="ExpandOrderRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="orderSize" type="xs:int"/><xs:element name="codeLength" type="xs:int"/><xs:element name="codePattern" type="CodePattern"/><xs:element minOccurs="0" name="codeCase" type="CodeCase"/><xs:element minOccurs="0" name="sorting" type="CodeSorting"/><xs:element minOccurs="0" name="name" type="ExpansionName"/></xs:sequence></xs:complexType></xs:element><xs:element name="ExpandOrderResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="orderRequestSequence" type="xs:int"/><xs:element name="downloadUrl" type="xs:anyURI"/><xs:element name="expansionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="MultiExpandOrderRequest"><xs:complexType><xs:sequence><xs:element name="expansion"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="orderSize" type="xs:int"/><xs:element name="codeLength" type="xs:int"/><xs:element name="codePattern" type="CodePattern"/><xs:element minOccurs="0" name="codeCase" type="CodeCase"/><xs:element minOccurs="0" name="name" type="ExpansionName"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="pairedExpansion"><xs:complexType><xs:sequence><xs:element name="codeLength" type="xs:int"/><xs:element name="codePattern" type="CodePattern"/><xs:element minOccurs="0" name="codeCase" type="CodeCase"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="repeats" type="xs:positiveInteger"/></xs:sequence></xs:complexType></xs:element><xs:element name="MultiExpandOrderResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" name="expansion"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="orderRequestSequence" type="xs:integer"/><xs:element name="downloadUrl" type="xs:anyURI"/><xs:element name="expansionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="ReadSsccRequest"><xs:complexType><xs:sequence><xs:element name="sscc" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadSsccResponse"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="orderId" type="xs:long"/><xs:element name="codeIndex" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadSsccSequenceRequest"><xs:complexType><xs:sequence><xs:element name="expansionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadSsccSequenceResponse"><xs:complexType><xs:sequence><xs:element name="start" type="xs:long"/><xs:element name="end" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="AddReservedSsccSequenceRequest"><xs:complexType><xs:sequence><xs:element name="start" type="xs:long"/><xs:element name="end" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="AddReservedSsccSequenceResponse"><xs:complexType><xs:sequence><xs:element name="start" type="xs:long"/><xs:element name="end" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteReservedSsccSequenceRequest"><xs:complexType><xs:sequence><xs:element name="start" type="xs:long"/><xs:element name="end" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteReservedSsccSequenceResponse"><xs:complexType><xs:sequence><xs:element name="start" type="xs:long"/><xs:element name="end" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ListReservedSsccSequenceRequest"><xs:complexType/></xs:element><xs:element name="ListReservedSsccSequenceResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="sequence"><xs:complexType><xs:sequence><xs:element name="start" type="xs:long"/><xs:element name="end" type="xs:long"/></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="CreateSsccSequenceRequest"><xs:complexType><xs:sequence><xs:element name="expansionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="CreateSsccSequenceResponse"><xs:complexType><xs:sequence><xs:element name="start" type="xs:long"/><xs:element name="end" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="SetExpansionStatusRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="sequence" type="xs:int"/><xs:element minOccurs="0" name="status" type="ExpansionStatusType"/></xs:sequence></xs:complexType></xs:element><xs:element name="SetExpansionStatusResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="ListExpansionsRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence><xs:attribute name="offset" type="xs:int"/><xs:attribute name="max" type="xs:int"/></xs:complexType></xs:element><xs:element name="ListExpansionsResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="expansion" type="OrderExpansion"/></xs:sequence><xs:attribute name="offset" type="xs:int"/><xs:attribute name="max" type="xs:int"/><xs:attribute name="totalRecords" type="xs:long"/></xs:complexType></xs:element><xs:element name="GetExpansionRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetExpansionResponse" type="OrderExpansion"/><xs:element name="ListAllExpansionsRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element name="startTime" type="xs:dateTime"/><xs:element name="endTime" type="xs:dateTime"/><xs:element minOccurs="0" name="organizationId" type="xs:int"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListAllExpansionsResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="expansion" type="OrderExpansion"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="GetCodesProducedByUserRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element name="startTime" type="xs:dateTime"/><xs:element name="endTime" type="xs:dateTime"/><xs:element minOccurs="0" name="organizationId" type="xs:int"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="GetCodesProducedByUserResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codes" type="CodesPerUser"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="GetCodesProducedByGroupRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element name="startTime" type="xs:dateTime"/><xs:element name="endTime" type="xs:dateTime"/><xs:element minOccurs="0" name="organizationId" type="xs:int"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="GetCodesProducedByGroupResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codes" type="CodesPerGroup"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="GetCodesProducedByProductRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element name="startTime" type="xs:dateTime"/><xs:element name="endTime" type="xs:dateTime"/><xs:element minOccurs="0" name="organizationId" type="xs:int"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="GetCodesProducedByProductResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codes" type="CodesPerProduct"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="DownloadCodesRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:choice><xs:element name="expansionId" type="xs:long"/><xs:element name="orderId" type="xs:long"/></xs:choice></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="DownloadCodesResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element minOccurs="0" name="expansionId" type="xs:long"/><xs:element name="codes" type="StringValueList"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListExpansionCodesRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="sequence" type="xs:int"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListExpansionCodesResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="code" type="CodeData"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ExpansionsStatusRequest"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="sequence" type="xs:int"/></xs:sequence><xs:attribute name="orderId" type="xs:long"/></xs:complexType></xs:element><xs:element name="ExpansionsStatusResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="expansionStatus" type="ExpansionStatus"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetOrderExpansionsValidationsRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetOrderExpansionsValidationsResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="expansionValidations" type="ExpansionValidations"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteLastExpansionRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteLastExpansionResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetOrderValidationsRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetOrderValidationsResponse"><xs:complexType><xs:sequence><xs:element name="total" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetOrderCodeStatusStatisticsRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetOrderCodeStatusStatisticsResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="status" type="CodeStatusStatistics"/></xs:sequence></xs:complexType></xs:element><xs:simpleType name="EntryChannelType"><xs:restriction base="xs:string"><xs:enumeration value="SMS"/><xs:enumeration value="WEB"/></xs:restriction></xs:simpleType><xs:simpleType name="StringValueList"><xs:list itemType="xs:string"/></xs:simpleType><xs:simpleType name="CharacterType"><xs:restriction base="xs:string"><xs:pattern value="[a-zA-Z]"/></xs:restriction></xs:simpleType><xs:simpleType name="CodeStatusType"><xs:restriction base="xs:string"><xs:enumeration value="BASIC_8"/><xs:enumeration value="BASIC_16"/><xs:enumeration value="TIMESTAMP_8"/><xs:enumeration value="TIMESTAMP_16"/></xs:restriction></xs:simpleType><xs:complexType name="CodeStatusField"><xs:sequence><xs:element name="id" type="xs:int"/><xs:element minOccurs="0" name="builtin" type="xs:boolean"/><xs:element name="description" type="xs:string"/></xs:sequence><xs:attribute name="validatable" type="xs:boolean"/><xs:attribute name="packable" type="xs:boolean"/><xs:attribute name="settable" type="xs:boolean"/><xs:attribute name="unsettable" type="xs:boolean"/></xs:complexType><xs:complexType name="OutputCode"><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="orderId" type="xs:long"/><xs:element name="codeIndex" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="OtherProductIdType"><xs:sequence><xs:element name="otherProductId" type="xs:string"/></xs:sequence><xs:attribute name="type" type="xs:string"/></xs:complexType><xs:complexType name="ProductSummary"><xs:sequence><xs:element name="productId" type="xs:long"/><xs:element name="name" type="xs:string"/></xs:sequence></xs:complexType><xs:complexType name="Product"><xs:sequence><xs:element name="productId" type="xs:long"/><xs:element name="name" type="xs:string"/><xs:element minOccurs="0" name="gtin" type="xs:string"/><xs:element minOccurs="0" name="otherProductId" type="OtherProductIdType"/><xs:element minOccurs="0" name="alias" type="xs:string"/><xs:element minOccurs="0" name="customerProductReference" type="xs:string"/><xs:element minOccurs="0" name="netWeight" type="xs:decimal"/><xs:element minOccurs="0" name="atiGroupId" type="xs:long"/><xs:element minOccurs="0" name="atiGroupName" type="xs:string"/><xs:element minOccurs="0" name="metadataSchemaId" type="xs:int"/><xs:element minOccurs="0" name="packageTypeId" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="CreateProduct"><xs:sequence><xs:element name="name" type="xs:string"/><xs:element minOccurs="0" name="gtin" type="xs:string"/><xs:element minOccurs="0" name="otherProductId" type="OtherProductIdType"/><xs:element minOccurs="0" name="alias" type="xs:string"/><xs:element minOccurs="0" name="customerProductReference" type="xs:string"/><xs:element minOccurs="0" name="atiGroupId" type="xs:long"/><xs:element minOccurs="0" name="packageTypeId" type="xs:long"/></xs:sequence></xs:complexType><xs:simpleType name="ExpansionStatusType"><xs:restriction base="xs:string"><xs:enumeration value="LFP"/><xs:enumeration value="P"/></xs:restriction></xs:simpleType><xs:simpleType name="CodeCase"><xs:restriction base="xs:string"><xs:enumeration value="UPPERCASE"/><xs:enumeration value="LOWERCASE"/></xs:restriction></xs:simpleType><xs:simpleType name="ShadowCodeStatus"><xs:restriction base="xs:string"><xs:enumeration value="ADMINISTRATIVE"/><xs:enumeration value="CONSUMER"/></xs:restriction></xs:simpleType><xs:complexType name="OrderExpansion"><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="orderId" type="xs:long"/><xs:element name="sequence" type="xs:int"/><xs:element name="codePattern" type="CodePattern"/><xs:element name="sorting" type="CodeSorting"/><xs:element name="orderSize" type="xs:long"/><xs:element name="startIndex" type="xs:long"/><xs:element name="endIndex" type="xs:long"/><xs:element name="codeLength" type="xs:int"/><xs:element name="created" type="xs:dateTime"/><xs:element minOccurs="0" name="started" type="xs:dateTime"/><xs:element minOccurs="0" name="completed" type="xs:dateTime"/><xs:element minOccurs="0" name="removed" type="xs:dateTime"/><xs:element minOccurs="0" name="codeCase" type="CodeCase"/><xs:element minOccurs="0" name="name" type="ExpansionName"/><xs:element minOccurs="0" name="status" type="ExpansionStatusType"/><xs:element minOccurs="0" name="shadowStatus" type="ShadowCodeStatus"/><xs:element minOccurs="0" name="createdBy" type="xs:string"/><xs:element minOccurs="0" name="createdByGroup" type="xs:string"/></xs:sequence></xs:complexType><xs:complexType name="CodeData"><xs:sequence><xs:element name="text" type="xs:string"/><xs:element minOccurs="0" name="statuses"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" name="status" type="CodeStatus"/></xs:sequence></xs:complexType></xs:element></xs:sequence><xs:attribute name="index" type="xs:long"/></xs:complexType><xs:simpleType name="CodePattern"><xs:restriction base="xs:string"><xs:minLength value="1"/></xs:restriction></xs:simpleType><xs:simpleType name="ExpansionName"><xs:restriction base="xs:string"><xs:maxLength value="32"/><xs:minLength value="0"/></xs:restriction></xs:simpleType><xs:complexType name="ExpansionStatus"><xs:sequence><xs:element name="sequence" type="xs:int"/><xs:element name="operation" type="xs:string"/><xs:element name="progress" type="xs:double"/></xs:sequence></xs:complexType><xs:complexType name="ExpansionValidations"><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="validations" type="xs:long"/><xs:element name="expansionSize" type="xs:long"/></xs:sequence></xs:complexType><xs:simpleType name="CodeSorting"><xs:restriction base="xs:string"><xs:enumeration value="R"/><xs:enumeration value="A"/><xs:enumeration value="D"/></xs:restriction></xs:simpleType><xs:element name="order" type="Order"/><xs:complexType name="Order"><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="type" type="OrderType"/><xs:element name="size" type="xs:long"/><xs:element name="created" type="xs:dateTime"/><xs:element name="isLocked" type="xs:boolean"/><xs:element minOccurs="0" name="description" type="xs:string"/><xs:element name="owner" type="ns1:SummarySid"/><xs:element minOccurs="0" name="product" type="Product"/><xs:element minOccurs="0" name="metadataSchema" type="xs:string"/><xs:element name="metadataPresent" type="xs:boolean"/><xs:element default="false" minOccurs="0" name="sectioned" type="xs:boolean"/><xs:element minOccurs="0" name="createdBy" type="xs:string"/></xs:sequence></xs:complexType><xs:simpleType name="OrderType"><xs:restriction base="xs:string"><xs:enumeration value="m"/><xs:enumeration value="p"/><xs:enumeration value="s"/></xs:restriction></xs:simpleType><xs:complexType name="SectionCreate"><xs:sequence><xs:element minOccurs="0" name="id" type="xs:long"/><xs:element name="orderId" type="xs:long"/><xs:element name="startIndex" type="xs:long"/><xs:element name="endIndex" type="xs:long"/><xs:element minOccurs="0" name="activateDate" type="xs:dateTime"/><xs:element minOccurs="0" name="deactivateDate" type="xs:dateTime"/><xs:element name="maxValidations" type="xs:integer"/><xs:element name="enabled" type="xs:boolean"/><xs:element minOccurs="0" name="comment" type="xs:string"/><xs:element minOccurs="0" name="productId" type="xs:long"/><xs:element minOccurs="0" name="metadataSchema" type="xs:string"/></xs:sequence></xs:complexType><xs:complexType name="SectionsStatistics"><xs:sequence><xs:element name="activeSections" type="xs:int"/><xs:element name="nonActiveSections" type="xs:int"/><xs:element name="activeCodes" type="xs:long"/><xs:element name="nonActiveCodes" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="Section"><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="orderId" type="xs:long"/><xs:element name="startIndex" type="xs:long"/><xs:element minOccurs="0" name="startCode" type="xs:string"/><xs:element name="endIndex" type="xs:long"/><xs:element minOccurs="0" name="endCode" type="xs:string"/><xs:element minOccurs="0" name="activateDate" type="xs:dateTime"/><xs:element minOccurs="0" name="deactivateDate" type="xs:dateTime"/><xs:element minOccurs="0" name="activateOrderedDate" type="xs:dateTime"/><xs:element minOccurs="0" name="activatedBy" type="ns1:OutputUser"/><xs:element name="maxValidations" type="xs:integer"/><xs:element name="enabled" type="xs:boolean"/><xs:element minOccurs="0" name="comment" type="xs:string"/><xs:element minOccurs="0" name="product" type="Product"/><xs:element minOccurs="0" name="metadataSchema" type="xs:string"/><xs:element minOccurs="0" name="atiCount" type="xs:long"/><xs:element minOccurs="0" name="rollId" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="Roll"><xs:sequence><xs:element name="codesCountInActiveStretches" type="xs:long"/><xs:element name="activeStretchesCount" type="xs:long"/><xs:element name="startIndex" type="xs:long"/><xs:element name="endIndex" type="xs:long"/><xs:element name="tempEndIndex" type="xs:long"/><xs:element name="full" type="xs:boolean"/><xs:element minOccurs="0" name="lastActivationOrdered" type="xs:dateTime"/><xs:element minOccurs="0" name="asc" type="xs:boolean"/></xs:sequence></xs:complexType><xs:complexType name="FullRoll"><xs:sequence><xs:element name="rollId" type="xs:long"/><xs:element name="orderId" type="xs:long"/><xs:element name="ascending" type="xs:boolean"/><xs:element name="startIndex" type="xs:long"/><xs:element name="endIndex" type="xs:long"/><xs:element name="sections"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="section" type="Section"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="unassigned"><xs:complexType><xs:sequence><xs:element name="startIndex" type="xs:long"/><xs:element name="endIndex" type="xs:long"/></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:complexType><xs:complexType name="Ati"><xs:sequence><xs:element minOccurs="0" name="id" type="xs:long"/><xs:element name="name" type="xs:string"/><xs:element name="type" type="AtiType"/><xs:element name="webMessage" type="xs:string"/><xs:element name="smsMessage" type="xs:string"/><xs:element name="translations" type="AtiTranslations"/><xs:element minOccurs="0" name="activate" type="xs:string"/><xs:element minOccurs="0" name="deactivate" type="xs:string"/><xs:element name="validationsRangeStart" type="xs:int"/><xs:element minOccurs="0" name="validationsRangeEnd" type="xs:int"/></xs:sequence></xs:complexType><xs:complexType name="AtiTranslations"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="translation"><xs:complexType><xs:sequence><xs:element name="country" type="xs:string"/><xs:element minOccurs="0" name="webMessage" type="xs:string"/><xs:element minOccurs="0" name="smsMessage" type="xs:string"/></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:complexType><xs:complexType name="AttachedAti"><xs:complexContent><xs:extension base="Ati"><xs:sequence><xs:element name="isActive" type="xs:boolean"/><xs:element minOccurs="0" name="activeFrom" type="xs:dateTime"/><xs:element minOccurs="0" name="activeTo" type="xs:dateTime"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType><xs:complexType name="AtiGroup"><xs:sequence><xs:element minOccurs="0" name="id" type="xs:long"/><xs:element name="name" type="xs:string"/><xs:element name="atis"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="ati" type="Ati"/></xs:sequence></xs:complexType></xs:element></xs:sequence><xs:attribute default="false" name="default" type="xs:boolean" use="optional"/></xs:complexType><xs:complexType name="InputAtiGroup"><xs:sequence><xs:element minOccurs="0" name="id" type="xs:long"/><xs:element name="name" type="xs:string"/><xs:element name="atiIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element></xs:sequence><xs:attribute default="false" name="default" type="xs:boolean" use="optional"/></xs:complexType><xs:simpleType name="AtiType"><xs:restriction base="xs:string"><xs:enumeration value="f"/><xs:enumeration value="w"/><xs:enumeration value="n"/></xs:restriction></xs:simpleType><xs:complexType name="MetadataSchemaDescription"><xs:sequence><xs:element name="organization" type="xs:string"/><xs:element name="name" type="xs:string"/><xs:element name="isDefault" type="xs:boolean"/><xs:element name="content" type="xs:string"/></xs:sequence><xs:attribute name="id" type="xs:int" use="optional"/></xs:complexType><xs:complexType name="ProductMetadataSchemaDescription"><xs:sequence><xs:element name="id" type="xs:int"/><xs:element name="name" type="xs:string"/><xs:element name="content" type="xs:string"/></xs:sequence></xs:complexType><xs:complexType name="SimpleCodeConfigSummary"><xs:simpleContent><xs:extension base="xs:positiveInteger"><xs:attribute name="pattern" type="xs:string" use="optional"/></xs:extension></xs:simpleContent></xs:complexType><xs:complexType name="EntryChannelSummary"><xs:simpleContent><xs:extension base="xs:string"><xs:attribute name="id" type="xs:int" use="required"/><xs:attribute name="type" type="xs:string" use="required"/></xs:extension></xs:simpleContent></xs:complexType><xs:complexType name="ValidationLogEntry"><xs:all><xs:element name="code" type="xs:string"/><xs:element name="channel" type="EntryChannelSummary"/><xs:element name="entry" type="xs:string"/><xs:element minOccurs="0" name="organization"><xs:complexType><xs:simpleContent><xs:extension base="xs:string"><xs:attribute name="id" type="xs:int"/></xs:extension></xs:simpleContent></xs:complexType></xs:element><xs:element name="user"><xs:complexType><xs:simpleContent><xs:extension base="xs:string"><xs:attribute name="id" type="xs:int"/></xs:extension></xs:simpleContent></xs:complexType></xs:element><xs:element minOccurs="0" name="userExtraInformation" type="UserExtraInformation"/><xs:element minOccurs="0" name="location"><xs:complexType><xs:sequence><xs:element name="country" type="xs:string"/><xs:element minOccurs="0" name="name" type="xs:string"/><xs:element minOccurs="0" name="coords"><xs:complexType><xs:attribute name="lat" type="xs:decimal"/><xs:attribute name="long" type="xs:decimal"/></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="occurred" type="xs:dateTime"/><xs:element minOccurs="0" name="orderId" type="xs:long"/><xs:element minOccurs="0" name="sectionId" type="xs:long"/><xs:element minOccurs="0" name="product" type="Product"/><xs:element minOccurs="0" name="validations" type="xs:int"/><xs:element minOccurs="0" name="maxValidations" type="xs:int"/><xs:element minOccurs="0" name="errorCode" type="xs:int"/><xs:element name="valid" type="xs:string"/></xs:all></xs:complexType><xs:complexType name="UserExtraInformation"><xs:sequence><xs:element minOccurs="0" name="phoneNumber" type="xs:string"/><xs:element minOccurs="0" name="email" type="xs:string"/></xs:sequence></xs:complexType><xs:complexType name="CodeStatusStatistics"><xs:sequence><xs:element name="id" type="xs:int"/><xs:element name="name" type="CodeStatus"/><xs:element name="count" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="CodeStatusSnapshot"><xs:sequence><xs:element name="statusId" type="xs:int"/><xs:element name="orderId" type="xs:long"/><xs:element name="count" type="xs:long"/><xs:element name="modified" type="xs:dateTime"/></xs:sequence></xs:complexType><xs:complexType name="CodeStatus"><xs:simpleContent><xs:extension base="xs:string"><xs:attribute name="id" type="xs:int"/></xs:extension></xs:simpleContent></xs:complexType><xs:simpleType name="CodeStatusFilterOperator"><xs:restriction base="xs:string"><xs:enumeration value="SET"/><xs:enumeration value="UNSET"/></xs:restriction></xs:simpleType><xs:complexType name="SectionValidations"><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="validations" type="xs:long"/><xs:element name="sectionSize" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="BatchValidationEntry"><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="status" type="xs:string"/><xs:element minOccurs="0" name="orderId" type="xs:long"/><xs:element minOccurs="0" name="sectionId" type="xs:long"/><xs:element minOccurs="0" name="validations" type="xs:int"/><xs:element minOccurs="0" name="maxValidations" type="xs:int"/></xs:sequence></xs:complexType><xs:simpleType name="ValidationType"><xs:restriction base="xs:string"><xs:enumeration value="NORMAL"/><xs:enumeration value="SUPERVISED"/></xs:restriction></xs:simpleType><xs:simpleType name="ValidationCountRelation"><xs:restriction base="xs:string"><xs:enumeration value="EXACTLY"/><xs:enumeration value="AT_LEAST"/><xs:enumeration value="AT_MOST"/></xs:restriction></xs:simpleType><xs:complexType name="ValidationsLogFilter"><xs:all><xs:element minOccurs="0" name="organizationId" type="xs:int"/><xs:element minOccurs="0" name="hideValid" type="xs:boolean"/><xs:element minOccurs="0" name="hideInvalid" type="xs:boolean"/><xs:element minOccurs="0" name="hideVerified" type="xs:boolean"/><xs:element minOccurs="0" name="occurredAfter" type="xs:dateTime"/><xs:element minOccurs="0" name="occurredBefore" type="xs:dateTime"/><xs:element minOccurs="0" name="codes"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="code" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="codeSimilarity" type="xs:float"/><xs:element minOccurs="0" name="ignoreCodeCase" type="xs:boolean"/><xs:element minOccurs="0" name="ips"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="ip" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="phoneNumbers"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="phoneNumber" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="orderIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="sectionIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="productIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="productId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="validationCount" type="ValidationCount"/><xs:element minOccurs="0" name="channelIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="channelId" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="validationType" type="ValidationType"/></xs:all><xs:attribute name="offset" type="xs:int" use="required"/><xs:attribute name="max" type="xs:positiveInteger" use="required"/></xs:complexType><xs:complexType name="ValidationCount"><xs:sequence><xs:element name="count" type="xs:int"/><xs:element name="relation" type="ValidationCountRelation"/></xs:sequence></xs:complexType><xs:complexType name="CodesPerUser"><xs:sequence><xs:element name="user" type="xs:string"/><xs:element name="codesCount" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="CodesPerGroup"><xs:sequence><xs:element name="group" type="xs:string"/><xs:element name="codesCount" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="CodesPerProduct"><xs:sequence><xs:element name="product" type="xs:string"/><xs:element name="codesCount" type="xs:long"/></xs:sequence></xs:complexType><xs:element name="ListProductsRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"/></xs:complexContent></xs:complexType></xs:element><xs:element name="ListProductsResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="product" type="Product"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="CreateProductRequest"><xs:complexType><xs:sequence><xs:element name="product" type="CreateProduct"/></xs:sequence></xs:complexType></xs:element><xs:element name="CreateProductResponse"><xs:complexType><xs:sequence><xs:element name="productId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateProductRequest"><xs:complexType><xs:sequence><xs:element name="product" type="Product"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateProductResponse"><xs:complexType><xs:sequence><xs:element name="productId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteProductRequest"><xs:complexType><xs:sequence><xs:element name="productId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteProductResponse"><xs:complexType><xs:sequence><xs:element name="productId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetProductRequest"><xs:complexType><xs:sequence><xs:choice><xs:element name="productId" type="xs:long"/><xs:element name="gtin" type="xs:string"/><xs:element name="otherProductId" type="xs:string"/><xs:element name="customerProductReference" type="xs:string"/><xs:element name="alias" type="xs:string"/></xs:choice></xs:sequence></xs:complexType></xs:element><xs:element name="GetProductResponse"><xs:complexType><xs:sequence><xs:element name="product" type="Product"/></xs:sequence></xs:complexType></xs:element><xs:element name="FindLookAlikeCodeRequest"><xs:annotation><xs:documentation>Used by support/operators to attempt to find a correct code by analyzing matches excluding typical typos</xs:documentation></xs:annotation><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"><xs:annotation><xs:documentation>The code to search for</xs:documentation></xs:annotation></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="FindLookAlikeCodeResponse"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"><xs:annotation><xs:documentation>The code that was searched for</xs:documentation></xs:annotation></xs:element><xs:element name="validCodes"><xs:annotation><xs:documentation>A list of codes that are similar and valid</xs:documentation></xs:annotation><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="code" type="OutputCode"/></xs:sequence><xs:attribute name="count" type="xs:int" use="required"/></xs:complexType></xs:element><xs:element name="verifiedCodes"><xs:annotation><xs:documentation>A list of codes that are similar and correct codes but not activated</xs:documentation></xs:annotation><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="code" type="OutputCode"/></xs:sequence><xs:attribute name="count" type="xs:int" use="required"/></xs:complexType></xs:element></xs:sequence><xs:attribute name="permutationsSearched" type="xs:int" use="required"><xs:annotation><xs:documentation>The number of permutations of the original code searched</xs:documentation></xs:annotation></xs:attribute></xs:complexType></xs:element><xs:element name="ListCodeConfigsRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"/></xs:complexContent></xs:complexType></xs:element><xs:element name="ListCodeConfigsResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codeConfig" type="CodeConfigSummary"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ReadCodeConfigRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadCodeConfigResponse" type="CodeConfig"/><xs:element name="CreateCodeConfigRequest" type="CodeConfig"/><xs:element name="CreateCodeConfigResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:complexType name="CodeConfigSummary"><xs:sequence><xs:element minOccurs="0" name="id" type="xs:int"><xs:annotation><xs:documentation>The ID of the code code configuration</xs:documentation></xs:annotation></xs:element><xs:element name="description" type="xs:string"><xs:annotation><xs:documentation>A text description of the code configuration</xs:documentation></xs:annotation></xs:element><xs:element name="defaultCodeLength" type="xs:positiveInteger"><xs:annotation><xs:documentation>The default code length of this code pattern</xs:documentation></xs:annotation></xs:element><xs:element name="minCodeLength" type="xs:positiveInteger"><xs:annotation><xs:documentation>The minimum code length allowed for this code pattern</xs:documentation></xs:annotation></xs:element><xs:element name="maxCodeLength" type="xs:positiveInteger"><xs:annotation><xs:documentation>The maximum code length allowed for this code pattern</xs:documentation></xs:annotation></xs:element><xs:element name="alphabet"><xs:annotation><xs:documentation>The possible characters in the code</xs:documentation></xs:annotation><xs:complexType><xs:simpleContent><xs:extension base="xs:string"><xs:attribute name="charCount" type="xs:int" use="required"/></xs:extension></xs:simpleContent></xs:complexType></xs:element></xs:sequence></xs:complexType><xs:complexType name="CodeConfig"><xs:complexContent><xs:extension base="CodeConfigSummary"><xs:sequence><xs:element name="rLen" type="xs:int"/><xs:element name="cLen" type="xs:int"/><xs:element name="sLen" type="xs:int"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType><xs:element name="CreateSectionRequest" type="SectionCreate"/><xs:element name="CreateSectionResponse"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadSectionRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadSectionResponse" type="Section"/><xs:element name="UpdateSectionRequest" type="SectionCreate"/><xs:element name="UpdateSectionResponse"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteSectionRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteSectionResponse"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ListSectionsRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListSectionsResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element name="statistics" type="SectionsStatistics"/><xs:element maxOccurs="unbounded" minOccurs="0" name="section" type="Section"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListAtisRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence/></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListAtisResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="ati" type="Ati"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListSectionAtisRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ListSectionAtisResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="ati" type="AttachedAti"/></xs:sequence></xs:complexType></xs:element><xs:element name="AddAtiRequest" type="Ati"/><xs:element name="AddAtiResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateAtiRequest" type="Ati"/><xs:element name="UpdateAtiResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteAtiRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteAtiResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadAtiRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadAtiResponse" type="Ati"/><xs:element name="UnlinkAtiRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="UnlinkAtiResponse"><xs:complexType/></xs:element><xs:element name="UnlinkAllAtisRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="UnlinkAllAtisResponse"><xs:complexType/></xs:element><xs:element name="ApplyAtiRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ApplyAtiResponse"><xs:complexType/></xs:element><xs:element name="ApplyAtiTemplateGroupRequest"><xs:annotation><xs:documentation>Unsupported. Use ApplyAtiRequest instead</xs:documentation></xs:annotation><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ApplyAtiTemplateGroupResponse"><xs:complexType/></xs:element><xs:element name="RenameAtiRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/><xs:element name="name" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="RenameAtiResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetOrderSectionsValidationsRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetOrderSectionsValidationsResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="sectionValidations" type="SectionValidations"/></xs:sequence></xs:complexType></xs:element><xs:element name="MapExpansionsToSectionsRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="MapExpansionsToSectionsResponse"><xs:complexType/></xs:element><xs:element name="ListAtiGroupsRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence/></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListAtiGroupsResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="atiGroup" type="AtiGroup"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="AddAtiGroupRequest" type="InputAtiGroup"/><xs:element name="AddAtiGroupResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ApplyAtiGroupRequest"><xs:complexType><xs:sequence><xs:element name="atiGroupId" type="xs:long"/><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ApplyAtiGroupResponse"><xs:complexType/></xs:element><xs:element name="ReadAtiGroupRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadAtiGroupResponse" type="AtiGroup"/><xs:element name="DefaultAtiGroupRequest"><xs:complexType/></xs:element><xs:element name="DefaultAtiGroupResponse"><xs:complexType><xs:sequence><xs:element minOccurs="0" name="defaultAtiGroup" type="AtiGroup"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateAtiGroupRequest" type="InputAtiGroup"/><xs:element name="UpdateAtiGroupResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteAtiGroupRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteAtiGroupResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ActivateSectionRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/><xs:element minOccurs="0" name="activateDate" type="xs:dateTime"/><xs:element minOccurs="0" name="productId" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element name="ActivateSectionResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="DeactivateSectionRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/><xs:element minOccurs="0" name="activateDate" type="xs:dateTime"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeactivateSectionResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="IdentifyRollRequest"><xs:complexType><xs:sequence><xs:element minOccurs="0" name="cfgId" type="xs:int"/><xs:element name="code" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="IdentifyRollResponse"><xs:complexType><xs:sequence><xs:element name="rollId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ActivateRollSectionRequest"><xs:complexType><xs:sequence><xs:element name="rollId" type="xs:long"/><xs:element minOccurs="0" name="cfgId" type="xs:int"/><xs:element minOccurs="0" name="code" type="xs:string"/><xs:element name="productId" type="xs:long"/><xs:element name="metadataSchemaId" type="xs:int"/><xs:element name="metadata" type="xs:string"/><xs:element minOccurs="0" name="activationDate" type="xs:dateTime"/></xs:sequence></xs:complexType></xs:element><xs:element name="ActivateRollSectionResponse"><xs:complexType><xs:sequence><xs:element name="rollId" type="xs:long"/><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetRollRequest"><xs:complexType><xs:sequence><xs:element name="rollId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetRollResponse"><xs:complexType><xs:sequence><xs:element name="roll" type="FullRoll"/></xs:sequence></xs:complexType></xs:element><xs:element name="CalibrateRollRequest"><xs:complexType><xs:sequence><xs:element minOccurs="0" name="cfgId" type="xs:int"/><xs:element name="firstCode" type="xs:string"/><xs:element name="secondCode" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="CalibrateRollResponse"><xs:complexType><xs:sequence><xs:element name="rollId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadRollRequest"><xs:complexType><xs:sequence><xs:element name="rollId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadRollResponse" type="Roll"/><xs:element name="MarkTemporaryRollEndRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/><xs:element name="temporaryEndIndex" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="MarkTemporaryRollEndResponse" type="Roll"/><xs:element name="CreateNewSectionInRollRequest"><xs:complexType><xs:sequence><xs:element name="rollId" type="xs:long"/><xs:element minOccurs="0" name="activateDate" type="xs:dateTime"/><xs:element minOccurs="0" name="productId" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element name="CreateNewSectionInRollResponse" type="Section"/><xs:element name="DeActivateSectionInRollRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeActivateSectionInRollResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="DeleteOrderMetadataRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteOrderMetadataResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteOrderSectionMetadataRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteOrderSectionMetadataResponse"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ListMetadataSchemasRequest"><xs:complexType><xs:sequence><xs:element minOccurs="0" name="organizationId" type="xs:int"/></xs:sequence><xs:attribute name="offset" type="xs:integer"/><xs:attribute name="max" type="xs:integer"/><xs:attribute name="includeJson" type="xs:boolean"/></xs:complexType></xs:element><xs:element name="ListMetadataSchemasResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="schema" type="MetadataSchemaDescription"/></xs:sequence><xs:attribute name="offset" type="xs:int"/><xs:attribute name="max" type="xs:int"/><xs:attribute name="totalRecords" type="xs:int"/></xs:complexType></xs:element><xs:element name="DeleteMetadataSchemaRequest"><xs:complexType><xs:sequence><xs:element name="name" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteMetadataSchemaResponse"><xs:complexType><xs:sequence><xs:element name="name" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="SetDefaultMetadataSchemaRequest"><xs:complexType><xs:sequence><xs:element minOccurs="0" name="name" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="SetDefaultMetadataSchemaResponse"><xs:complexType><xs:sequence><xs:element name="name" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="ListProductMetadataSchemasRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence/><xs:attribute name="includeJson" type="xs:boolean"/></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListProductMetadataSchemasResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="schema" type="ProductMetadataSchemaDescription"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="DeleteProductMetadataSchemaRequest"><xs:complexType><xs:sequence><xs:element name="name" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteProductMetadataSchemaResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="ReadOrderMetadataRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadOrderMetadataResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element minOccurs="0" name="payload" type="ns2:PayloadType"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadOrderSectionMetadataRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadOrderSectionMetadataResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="sectionId" type="xs:long"/><xs:element minOccurs="0" name="payload" type="ns2:PayloadType"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateOrderSectionMetadataRequest"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/><xs:element name="payload" type="ns2:PayloadType"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateOrderSectionMetadataResponse"><xs:complexType><xs:sequence><xs:element name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateOrderMetadataRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="payload" type="ns2:PayloadType"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateOrderMetadataResponse"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="AppCodeValidatorRequest"><xs:complexType><xs:sequence><xs:element name="channelId" type="xs:int"/><xs:element name="code" type="xs:string"/><xs:element minOccurs="0" name="authentication"><xs:complexType><xs:sequence><xs:element name="username" type="xs:string"/><xs:element name="password" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="location"><xs:complexType><xs:attribute name="lat" type="xs:decimal" use="required"/><xs:attribute name="lon" type="xs:decimal" use="required"/></xs:complexType></xs:element><xs:element minOccurs="0" name="locale" type="xs:string"/><xs:element minOccurs="0" name="phonenumber" type="xs:string"/><xs:element minOccurs="0" name="email" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="AppCodeValidatorResponse"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="valid" type="xs:boolean"/><xs:element name="message" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="CodeValidatorRequest"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="entryType" type="EntryChannelType"/><xs:element name="entryAlias" type="xs:string"/><xs:element name="entryId" type="xs:string"/><xs:element minOccurs="0" name="email" type="xs:string"/><xs:element minOccurs="0" name="phonenumber" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="CodeValidatorResponse"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="valid" type="xs:boolean"/><xs:element minOccurs="0" name="validationCount" type="xs:int"/><xs:element minOccurs="0" name="maxValidationCount" type="xs:int"/><xs:element minOccurs="0" name="product" type="Product"/><xs:element name="response" type="xs:string"/><xs:element name="organization" type="ns1:SummaryOrganization"/></xs:sequence></xs:complexType></xs:element><xs:element name="BatchCodeValidatorRequest"><xs:complexType><xs:sequence><xs:element name="codes" type="xs:string"/></xs:sequence><xs:attribute name="returnValid" type="xs:boolean"/><xs:attribute name="returnInvalid" type="xs:boolean"/></xs:complexType></xs:element><xs:element name="BatchCodeValidatorResponse"><xs:complexType><xs:sequence><xs:element name="invalid"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="code"><xs:complexType><xs:simpleContent><xs:extension base="xs:string"/></xs:simpleContent></xs:complexType></xs:element></xs:sequence><xs:attribute form="qualified" name="count" type="xs:integer" use="required"/></xs:complexType></xs:element><xs:element name="valid"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="code"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element minOccurs="0" name="atis"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="ati"><xs:complexType><xs:sequence><xs:element name="web" type="xs:string"/><xs:element name="sms" type="xs:string"/></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element></xs:sequence><xs:attribute form="qualified" name="count" type="xs:integer" use="required"/></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="GetCodeRequest"><xs:complexType><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="codeIndex" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetCodeResponse"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="CodeDissectorRequest"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="CodeDissectorResponse"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="valid" type="xs:boolean"/><xs:element minOccurs="0" name="orderId" type="xs:long"/><xs:element minOccurs="0" name="orderType" type="xs:string"/><xs:element minOccurs="0" name="owner" type="ns1:SummarySid"/><xs:element minOccurs="0" name="codeIndex" type="xs:long"/><xs:element minOccurs="0" name="sectionId" type="xs:long"/><xs:element minOccurs="0" name="sectionStart" type="xs:long"/><xs:element minOccurs="0" name="sectionEnd" type="xs:long"/><xs:element minOccurs="0" name="validated" type="xs:int"/><xs:element minOccurs="0" name="maxValidations" type="xs:int"/><xs:element minOccurs="0" name="details" type="xs:string"/><xs:element minOccurs="0" name="external" type="xs:boolean"/><xs:element minOccurs="0" name="pattern" type="xs:string"/><xs:element minOccurs="0" name="prefix" type="xs:string"/><xs:element minOccurs="0" name="length" type="xs:int"/><xs:element minOccurs="0" name="product" type="Product"/><xs:choice><xs:element minOccurs="0" name="hasShadow"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="index" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="isShadow"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element name="index" type="xs:long"/></xs:sequence></xs:complexType></xs:element></xs:choice><xs:element minOccurs="0" name="sscc" type="xs:string"/><xs:element minOccurs="0" name="statuses"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="status" type="CodeStatus"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="organization" type="xs:string"/><xs:element name="channels"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="channel" type="EntryChannelSummary"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="codeCfg" type="SimpleCodeConfigSummary"/></xs:sequence></xs:complexType></xs:element><xs:element name="CustomerCodeDissectorRequest"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element minOccurs="0" name="cfgId" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element name="CustomerCodeDissectorResponse"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/><xs:element minOccurs="0" name="orderId" type="xs:long"/><xs:element minOccurs="0" name="codeIndex" type="xs:long"/><xs:element minOccurs="0" name="sectionId" type="xs:long"/><xs:element minOccurs="0" name="section" type="Section"/></xs:sequence></xs:complexType></xs:element><xs:element name="CodeBlacklistRequest"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="CodeBlacklistResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="code" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="CodeBlacklistAddRequest"><xs:complexType><xs:sequence><xs:element name="codes" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="CodeBlacklistAddResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="CodeBlacklistRemoveRequest"><xs:complexType><xs:sequence><xs:element name="codes" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="CodeBlacklistRemoveResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="ValidationsLogFilterRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element minOccurs="0" name="organizationId" type="xs:int"/><xs:element minOccurs="0" name="hideValid" type="xs:boolean"/><xs:element minOccurs="0" name="hideInvalid" type="xs:boolean"/><xs:element minOccurs="0" name="hideVerified" type="xs:boolean"/><xs:element minOccurs="0" name="occurredAfter" type="xs:dateTime"/><xs:element minOccurs="0" name="occurredBefore" type="xs:dateTime"/><xs:element minOccurs="0" name="codes"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="code" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="codeSimilarity" type="xs:float"/><xs:element minOccurs="0" name="ignoreCodeCase" type="xs:boolean"/><xs:element minOccurs="0" name="ips"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="ip" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="phoneNumbers"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="phoneNumber" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="orderIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="orderId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="sectionIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="sectionId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="productIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="productId" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="validationCount" type="ValidationCount"/><xs:element minOccurs="0" name="channelIds"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="channelId" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element minOccurs="0" name="validationType" type="ValidationType"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ValidationsLogFilterResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="entryElement" type="ValidationLogEntry"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="BatchValidationDetailsRequest"><xs:complexType><xs:sequence><xs:element name="batchId" type="xs:string"/></xs:sequence><xs:attribute name="offset" type="xs:long"/><xs:attribute name="max" type="xs:positiveInteger"/></xs:complexType></xs:element><xs:element name="BatchValidationDetailsResponse"><xs:complexType><xs:sequence><xs:element name="batchId" type="xs:string"/><xs:element name="user" type="ns1:OutputUser"/><xs:element name="occurred" type="xs:dateTime"/><xs:element name="valid" type="xs:long"/><xs:element name="verified" type="xs:long"/><xs:element name="invalid" type="xs:long"/><xs:element name="entries"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="entry" type="BatchValidationEntry"/></xs:sequence></xs:complexType></xs:element></xs:sequence><xs:attribute name="offset" type="xs:long"/><xs:attribute name="max" type="xs:positiveInteger"/></xs:complexType></xs:element><xs:element name="BatchValidationsLogRequest"><xs:complexType><xs:attribute name="offset" type="xs:long" use="required"/><xs:attribute name="max" type="xs:positiveInteger" use="required"/><xs:attribute name="occurredAfter" type="xs:dateTime" use="optional"/><xs:attribute name="occurredBefore" type="xs:dateTime" use="optional"/></xs:complexType></xs:element><xs:element name="BatchValidationsLogResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="entryElement"><xs:complexType><xs:sequence><xs:element minOccurs="0" name="batchId" type="xs:string"/><xs:element name="user" type="ns1:OutputUser"/><xs:element name="occurred" type="xs:dateTime"/><xs:element name="valid" type="xs:long"/><xs:element name="verified" type="xs:long"/><xs:element name="invalid" type="xs:long"/></xs:sequence></xs:complexType></xs:element></xs:sequence><xs:attribute name="hasMore" type="xs:boolean" use="required"/></xs:complexType></xs:element><xs:element name="IPLocalizationRequest"><xs:complexType><xs:sequence><xs:element name="ip" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="IPLocalizationResponse"><xs:complexType><xs:sequence><xs:element name="ip" type="xs:string"/><xs:element name="hostname" type="xs:string"/><xs:element name="countryCode" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="StatisticsRequest"><xs:complexType><xs:attribute name="organizationId" type="xs:int" use="optional"/><xs:attribute name="startTime" type="xs:dateTime" use="optional"/><xs:attribute name="endTime" type="xs:dateTime" use="optional"/></xs:complexType></xs:element><xs:element name="StatisticsResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="entry" type="stat"/></xs:sequence></xs:complexType></xs:element><xs:element name="StatisticsLastOrdersRequest"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="StatisticsLastOrdersResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="order" type="Order"/></xs:sequence></xs:complexType></xs:element><xs:element name="StatisticsLastOrderedExpansionsRequest"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="StatisticsLastOrderedExpansionsResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="expansion" type="OrderExpansionWithOwner"/></xs:sequence></xs:complexType></xs:element><xs:element name="StatisticsLastProducedExpansionsRequest"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="StatisticsLastProducedExpansionsResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="expansion" type="OrderExpansionWithOwner"/></xs:sequence></xs:complexType></xs:element><xs:complexType name="OrderExpansionWithOwner"><xs:complexContent><xs:extension base="OrderExpansion"><xs:sequence><xs:element name="owner" type="ns1:SummarySid"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType><xs:complexType name="stat"><xs:sequence><xs:element name="orders" type="xs:long"/><xs:element name="expansions" type="xs:long"/><xs:element name="codes" type="xs:long"/><xs:element name="invalid" type="xs:long"/><xs:element name="verified" type="xs:long"/><xs:element name="valid" type="xs:long"/></xs:sequence><xs:attribute name="period" type="xs:string" use="required"/></xs:complexType><xs:complexType name="EntryChannel"><xs:sequence><xs:element minOccurs="0" name="id" type="xs:int"/><xs:element minOccurs="0" name="invalidMessage" type="xs:string"/><xs:element name="translations" type="EntryChannelTranslations"/><xs:element maxOccurs="unbounded" minOccurs="0" name="owner"><xs:complexType><xs:choice><xs:element name="organization" type="ns1:Organization"/><xs:element name="organizationId" type="xs:int"/></xs:choice></xs:complexType></xs:element><xs:element minOccurs="0" name="codeConfig"><xs:complexType><xs:sequence><xs:element name="id" type="xs:int"/></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:complexType><xs:complexType name="EntryChannelTranslations"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="translation"><xs:complexType><xs:sequence><xs:element name="country" type="xs:string"/><xs:element name="invalidMessage" type="xs:string"/></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:complexType><xs:complexType name="WebEntryChannel"><xs:complexContent><xs:extension base="EntryChannel"><xs:sequence><xs:element name="alias" type="xs:string"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType><xs:complexType name="SmsEntryChannel"><xs:complexContent><xs:extension base="EntryChannel"><xs:sequence><xs:element name="phonenumber" type="xs:string"/><xs:element minOccurs="0" name="prefix" type="xs:string"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType><xs:element name="CreateEntryChannelRequest"><xs:complexType><xs:sequence><xs:choice><xs:element name="webEntryChannel" type="WebEntryChannel"/><xs:element name="smsEntryChannel" type="SmsEntryChannel"/></xs:choice></xs:sequence></xs:complexType></xs:element><xs:element name="CreateEntryChannelResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateEntryChannelRequest"><xs:complexType><xs:sequence><xs:choice><xs:element name="webEntryChannel" type="WebEntryChannel"/><xs:element name="smsEntryChannel" type="SmsEntryChannel"/></xs:choice></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateEntryChannelResponse"><xs:complexType><xs:sequence><xs:element name="id" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateEntryChannelTranslationsRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:int"/><xs:element minOccurs="0" name="invalidMessage" type="xs:string"/><xs:element name="translations" type="EntryChannelTranslations"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateEntryChannelTranslationsResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="GetEntryChannelRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetEntryChannelResponse"><xs:complexType><xs:sequence><xs:choice><xs:element name="webEntryChannel" type="WebEntryChannel"/><xs:element name="smsEntryChannel" type="SmsEntryChannel"/></xs:choice></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteEntryChannelRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:int"/></xs:sequence></xs:complexType></xs:element><xs:element name="DeleteEntryChannelResponse"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="ListEntryChannelsRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence/></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="ListEntryChannelsResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element name="entryChannels"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="entryChannel" type="EntryChannel"/></xs:sequence></xs:complexType></xs:element></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="DiskUsageRequest"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="DiskUsageResponse"><xs:complexType><xs:sequence><xs:element name="path" type="xs:string"/><xs:element name="totalDiskSpace" type="xs:long"/><xs:element name="availableDiskSpace" type="xs:long"/><xs:element name="kcengineFilesCount" type="xs:long"/><xs:element name="kcengineFilesSize" type="xs:long"/></xs:sequence></xs:complexType></xs:element><xs:element name="WorkersInfoRequest"/><xs:element name="WorkersInfoResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="worker" type="worker"/></xs:sequence><xs:attribute name="awaitingProduction" type="xs:long" use="required"/><xs:attribute name="productionRate" type="xs:double" use="required"/><xs:attribute name="productionSpeed" type="xs:double" use="required"/><xs:attribute name="workerThreads" type="xs:long" use="required"/></xs:complexType></xs:element><xs:element name="ExpansionsInfoRequest"><xs:complexType><xs:sequence/></xs:complexType></xs:element><xs:element name="ExpansionsInfoResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="queuedExpansion" type="queuedExpansion"/><xs:element maxOccurs="unbounded" minOccurs="0" name="strayExpansion" type="strayExpansion"/></xs:sequence></xs:complexType></xs:element><xs:complexType name="queuedExpansion"><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="sequenceNumber" type="xs:long"/><xs:element name="codeCount" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="strayExpansion"><xs:sequence><xs:element name="orderId" type="xs:long"/><xs:element name="sequenceNumber" type="xs:long"/><xs:element name="codeCount" type="xs:long"/></xs:sequence></xs:complexType><xs:complexType name="worker"><xs:sequence><xs:element name="name" type="xs:string"/><xs:element name="threads" type="xs:long"/><xs:element name="productionRate" type="xs:double"/></xs:sequence></xs:complexType><xs:complexType name="CodeStatusCount"><xs:attribute name="id" type="xs:int"/><xs:attribute name="name" type="xs:string"/><xs:attribute name="count" type="xs:int"/></xs:complexType><xs:complexType name="CodeStatusDelta"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="delta"><xs:complexType><xs:sequence><xs:element name="changed"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codestatus" type="CodeStatusCount"/></xs:sequence></xs:complexType></xs:element><xs:element name="skipped"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codestatus" type="CodeStatusCount"/></xs:sequence></xs:complexType></xs:element></xs:sequence><xs:attribute name="orderId" type="xs:long" use="required"/></xs:complexType></xs:element></xs:sequence></xs:complexType><xs:element name="UpdateCodeStatusConfigRequest"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codeStatusField" type="CodeStatusField"/></xs:sequence></xs:complexType></xs:element><xs:element name="UpdateCodeStatusConfigResponse"><xs:complexType/></xs:element><xs:element name="ReadCodeStatusConfigRequest"><xs:complexType><xs:sequence><xs:element name="id" type="xs:integer"/></xs:sequence></xs:complexType></xs:element><xs:element name="ReadCodeStatusConfigResponse"><xs:complexType><xs:sequence><xs:element name="codeStatusField" type="CodeStatusField"/></xs:sequence></xs:complexType></xs:element><xs:element name="AddCodeStatusConfigRequest"><xs:complexType><xs:sequence><xs:element name="codeStatusField" type="CodeStatusField"/></xs:sequence></xs:complexType></xs:element><xs:element name="AddCodeStatusConfigResponse"><xs:complexType/></xs:element><xs:element name="GetCodeStatusConfigRequest"><xs:complexType/></xs:element><xs:element name="GetCodeStatusConfigResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codeStatusField" type="CodeStatusField"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetCodeStatusHistoryRequest"><xs:complexType><xs:sequence><xs:element name="code" type="xs:string"/></xs:sequence></xs:complexType></xs:element><xs:element name="GetCodeStatusHistoryResponse"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codeStatusSet"><xs:complexType><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codeStatuses" type="CodeStatus"/></xs:sequence><xs:attribute name="timestamp" type="xs:dateTime"/></xs:complexType></xs:element></xs:sequence></xs:complexType></xs:element><xs:element name="GetCodeStatusChangesRequest"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageRequest"><xs:sequence><xs:element name="from" type="xs:dateTime"/><xs:element minOccurs="0" name="to" type="xs:dateTime"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="GetCodeStatusChangesResponse"><xs:complexType><xs:complexContent><xs:extension base="ns0:PageResponse"><xs:sequence><xs:element maxOccurs="unbounded" minOccurs="0" name="codeStatusSet" type="CodeStatusSnapshot"/></xs:sequence></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:complexType name="AnyOrderCodeStatus"><xs:sequence><xs:element name="statuses"><xs:simpleType><xs:list itemType="xs:int"/></xs:simpleType></xs:element><xs:element name="codes"><xs:simpleType><xs:list itemType="xs:string"/></xs:simpleType></xs:element></xs:sequence><xs:attribute default="true" name="ignoreInvalidCodes" type="xs:boolean"/></xs:complexType><xs:complexType name="CodeStatusResult"><xs:sequence><xs:element name="delta" type="CodeStatusDelta"/><xs:element name="invalidCodes"><xs:simpleType><xs:list itemType="xs:string"/></xs:simpleType></xs:element></xs:sequence><xs:attribute name="additionalPairedCodes" type="xs:int"/></xs:complexType><xs:element name="SetCodeStatusRequest" type="AnyOrderCodeStatus"/><xs:element name="SetCodeStatusResponse" type="CodeStatusResult"/><xs:element name="SetCodeStatusForOrderRequest"><xs:complexType><xs:complexContent><xs:extension base="AnyOrderCodeStatus"><xs:attribute name="orderId" type="xs:long" use="required"/><xs:attribute name="applyToRemaining" type="xs:boolean"/></xs:extension></xs:complexContent></xs:complexType></xs:element><xs:element name="SetCodeStatusForOrderResponse" type="CodeStatusResult"/></xs:schema>
    <schema xmlns="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://kezzlerssp.com/schemas/security" attributeFormDefault="unqualified" elementFormDefault="qualified" targetNamespace="http://kezzlerssp.com/schemas/security"><complexType name="Authentication"><sequence><element minOccurs="0" name="ip" type="string"/><element name="username" type="string"/><element name="time" type="dateTime"/><element minOccurs="0" name="userAgent" type="string"/></sequence><attribute name="eventType" type="string" use="required"/></complexType><complexType name="Organization"><sequence><element minOccurs="0" name="id" type="int"/><element name="name" type="string"/><element name="email" type="string"/><element minOccurs="0" name="adminUser" type="string"/><element minOccurs="0" name="gs1Prefix" type="string"/></sequence></complexType><complexType name="GroupCreate"><sequence><element name="name" type="string"/><element minOccurs="0" name="parentId" type="int"/><element name="roles"><complexType><sequence><element maxOccurs="unbounded" minOccurs="0" name="role" type="tns:GrantedAuthority"/></sequence></complexType></element></sequence><attribute name="representation" type="string" use="optional"/></complexType><complexType name="GroupUpdate"><complexContent><extension base="tns:GroupCreate"><sequence><element minOccurs="0" name="id" type="int"/></sequence></extension></complexContent></complexType><complexType name="Group"><complexContent><extension base="tns:GroupUpdate"><sequence><element name="organization"><complexType><sequence><element name="name" type="string"/></sequence><attribute name="id" type="int" use="required"/></complexType></element></sequence></extension></complexContent></complexType><complexType name="GrantedAuthority"><simpleContent><extension base="string"><attribute name="implicit" type="boolean"/></extension></simpleContent></complexType><complexType name="User"><sequence><element minOccurs="0" name="id" type="int"/><element name="username" type="string"/><element name="email" type="string"/><element minOccurs="0" name="organizationId" type="int"/><element name="enabled" type="boolean"/><element name="credentialsExpired" type="boolean"/><element name="locked" type="boolean"/><element name="defaultGroup"><complexType><sequence><element name="id" type="int"/><element name="name" type="string"/></sequence></complexType></element><element minOccurs="0" name="phoneNumbers"><complexType><sequence><element maxOccurs="unbounded" minOccurs="0" name="phoneNumber" type="string"/></sequence></complexType></element></sequence></complexType><complexType name="InputUser"><sequence><element minOccurs="0" name="id" type="int"/><element name="username" type="string"/><element name="email" type="string"/><element name="enabled" type="boolean"/><element name="locked" type="boolean"/><element name="defaultGroupId" type="int"/><element minOccurs="0" name="plainPassword" type="string"/><element minOccurs="0" name="phoneNumbers"><complexType><sequence><element maxOccurs="unbounded" minOccurs="0" name="phoneNumber" type="string"/></sequence></complexType></element></sequence></complexType><complexType name="OutputUser"><sequence><element minOccurs="0" name="id" type="int"/><element name="username" type="string"/><element name="email" type="string"/><element name="organization" type="tns:Organization"/></sequence></complexType><complexType name="InputUserCertificateMapping"><sequence><element name="certificate" type="tns:InputUserCertificate"/></sequence></complexType><complexType name="OuputUserCertificateMapping"><sequence><element name="user" type="tns:OutputUser"/><element name="certificate" type="tns:InputUserCertificate"/></sequence><attribute name="active" type="boolean" use="required"/></complexType><complexType name="InputUserCertificate"><sequence><element name="issuerCN" type="string"/><element name="certSerial" type="integer"/></sequence></complexType><complexType name="UserPreferences"><sequence><choice><element name="userId" type="int"/><element name="userName" type="string"/></choice><element name="timezone" type="string"/></sequence></complexType><complexType abstract="true" name="AbstractPermission"><sequence><element name="permissions"><complexType><attribute name="read" type="boolean"/><attribute name="update" type="boolean"/><attribute name="delete" type="boolean"/><attribute name="admin" type="boolean"/></complexType></element></sequence><attribute default="true" name="isGranting" type="boolean"/><attribute name="isOwner" type="boolean"/></complexType><complexType name="ReadPermission"><complexContent><extension base="tns:AbstractPermission"><sequence><element name="sid" type="tns:Sid"/></sequence></extension></complexContent></complexType><complexType name="PermissionResponse"><sequence><element name="object" type="tns:ObjectId"/><element name="aces"><complexType><sequence><element maxOccurs="unbounded" minOccurs="0" name="ace" type="tns:ReadPermission"/></sequence></complexType></element></sequence></complexType><complexType name="CreatePermission"><complexContent><extension base="tns:AbstractPermission"><sequence><element name="sid"><complexType><sequence><choice><element name="userId" type="int"/><element name="groupId" type="int"/><element name="organizationId" type="int"/></choice></sequence></complexType></element></sequence></extension></complexContent></complexType><complexType name="ObjectId"><sequence><element name="id" type="long"/><element name="type" type="string"/></sequence></complexType><complexType name="Sid"><sequence><choice><element name="user" type="tns:User"/><element name="group" type="tns:Group"/><element name="organization" type="tns:Organization"/></choice></sequence></complexType><complexType name="SummaryOrganization"><sequence><element name="id" type="int"/><element name="name" type="string"/></sequence></complexType><complexType name="SummaryGroup"><sequence><element name="id" type="int"/><element name="name" type="string"/><element name="organizationId" type="int"/></sequence></complexType><complexType name="SummaryUser"><sequence><element name="id" type="int"/><element name="username" type="string"/><element name="organizationId" type="int"/><element name="organizationName" type="string"/></sequence></complexType><complexType name="SummarySid"><sequence><choice><element name="user" type="tns:SummaryUser"/><element name="group" type="tns:SummaryGroup"/><element name="organization" type="tns:SummaryOrganization"/></choice></sequence></complexType><complexType name="IpBan"><sequence><element name="ip" type="string"/><element name="issued" type="dateTime"/><element name="expires" type="dateTime"/><element name="reason" type="string"/></sequence></complexType></schema>
    <schema xmlns="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://kezzlerssp.com/schemas/common" attributeFormDefault="unqualified" elementFormDefault="qualified" targetNamespace="http://kezzlerssp.com/schemas/common"><complexType abstract="true" name="PageRequest"><sequence><element minOccurs="0" name="sorting"><complexType><sequence><element maxOccurs="unbounded" minOccurs="0" name="sortBy"><complexType><simpleContent><extension base="string"><attribute name="asc" type="boolean"/></extension></simpleContent></complexType></element></sequence></complexType></element></sequence><attribute default="0" name="offset" type="nonNegativeInteger"><annotation><documentation>The offset in result set</documentation></annotation></attribute><attribute default="25" name="max"><annotation><documentation>The maximum number of results to return in the result set</documentation></annotation><simpleType><restriction base="integer"><maxInclusive value="20000"/></restriction></simpleType></attribute></complexType><complexType abstract="true" name="PageResponse"><sequence/><attribute name="offset" type="int" use="required"><annotation><documentation>The offset used when fetching this result set</documentation></annotation></attribute><attribute name="max" type="int" use="required"><annotation><documentation>The maximum number of results allowed according to the request</documentation></annotation></attribute><attribute name="hasMore" type="boolean" use="required"><annotation><documentation>True if there are more results available</documentation></annotation></attribute><attribute name="totalRecords" type="long" use="optional"><annotation><documentation>The number of items available in total
....</documentation></annotation></attribute></complexType><complexType name="ThreeDimension"><sequence><element name="length" type="decimal"/><element name="height" type="decimal"/><element name="width" type="decimal"/></sequence></complexType><simpleType name="SortOrder"><restriction base="string"><enumeration value="ASC"/><enumeration value="DESC"/></restriction></simpleType><complexType name="QueuedJobType"><sequence><element name="jobId" type="string"/><element name="jobType" type="string"/><element name="created" type="dateTime"/><element minOccurs="0" name="started" type="dateTime"/><element minOccurs="0" name="completed" type="dateTime"/><element minOccurs="0" name="resourceUrl" type="anyURI"/><element minOccurs="0" name="returnUrl" type="anyURI"/><element minOccurs="0" name="result"><complexType><choice><element name="success"><complexType><sequence/></complexType></element><element name="failure"><complexType><sequence><element minOccurs="0" name="errorCode" type="string"/><element name="errorMessage" type="string"/></sequence></complexType></element></choice></complexType></element><element name="progressInfo"><complexType><sequence><element name="stages"><complexType><sequence><element maxOccurs="unbounded" name="stage"><complexType><simpleContent><extension base="string"><attribute name="active" type="boolean"/><attribute name="progress" type="double"/></extension></simpleContent></complexType></element></sequence></complexType></element></sequence></complexType></element><element minOccurs="0" name="extra"><complexType><sequence><element maxOccurs="unbounded" name="entry"><complexType><sequence><element name="name" type="string"/><element name="value" type="string"/></sequence></complexType></element></sequence></complexType></element></sequence></complexType></schema>
    <xs:schema xmlns="http://example.com/fns" xmlns:tns="http://kezzlerssp.com/schema/metadata/foreign/" xmlns:xs="http://www.w3.org/2001/XMLSchema" attributeFormDefault="unqualified" elementFormDefault="qualified" targetNamespace="http://kezzlerssp.com/schema/metadata/foreign/"><xs:complexType name="PayloadType"><xs:sequence><xs:choice maxOccurs="unbounded"><xs:any namespace="##other" processContents="skip"/><xs:any namespace="##local" processContents="skip"/></xs:choice></xs:sequence></xs:complexType></xs:schema>
  </wsdl:types>
  <wsdl:message name="ApplyAtiTemplateGroupRequest">
    <wsdl:part element="tns:ApplyAtiTemplateGroupRequest" name="ApplyAtiTemplateGroupRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateEntryChannelResponse">
    <wsdl:part element="tns:CreateEntryChannelResponse" name="CreateEntryChannelResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadCodeConfigResponse">
    <wsdl:part element="tns:ReadCodeConfigResponse" name="ReadCodeConfigResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListSectionsRequest">
    <wsdl:part element="tns:ListSectionsRequest" name="ListSectionsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetOrderSectionsValidationsResponse">
    <wsdl:part element="tns:GetOrderSectionsValidationsResponse" name="GetOrderSectionsValidationsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ActivateRollSectionResponse">
    <wsdl:part element="tns:ActivateRollSectionResponse" name="ActivateRollSectionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateProductResponse">
    <wsdl:part element="tns:CreateProductResponse" name="CreateProductResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadCodeConfigRequest">
    <wsdl:part element="tns:ReadCodeConfigRequest" name="ReadCodeConfigRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodeRequest">
    <wsdl:part element="tns:GetCodeRequest" name="GetCodeRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadSsccResponse">
    <wsdl:part element="tns:ReadSsccResponse" name="ReadSsccResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="MultiExpandOrderResponse">
    <wsdl:part element="tns:MultiExpandOrderResponse" name="MultiExpandOrderResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadAtiResponse">
    <wsdl:part element="tns:ReadAtiResponse" name="ReadAtiResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeBlacklistAddResponse">
    <wsdl:part element="tns:CodeBlacklistAddResponse" name="CodeBlacklistAddResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadCodeStatusConfigRequest">
    <wsdl:part element="tns:ReadCodeStatusConfigRequest" name="ReadCodeStatusConfigRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListExpansionCodesResponse">
    <wsdl:part element="tns:ListExpansionCodesResponse" name="ListExpansionCodesResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListAtisResponse">
    <wsdl:part element="tns:ListAtisResponse" name="ListAtisResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListAtiGroupsRequest">
    <wsdl:part element="tns:ListAtiGroupsRequest" name="ListAtiGroupsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateAtiGroupResponse">
    <wsdl:part element="tns:UpdateAtiGroupResponse" name="UpdateAtiGroupResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ExpandOrderResponse">
    <wsdl:part element="tns:ExpandOrderResponse" name="ExpandOrderResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodesProducedByGroupRequest">
    <wsdl:part element="tns:GetCodesProducedByGroupRequest" name="GetCodesProducedByGroupRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodesProducedByGroupResponse">
    <wsdl:part element="tns:GetCodesProducedByGroupResponse" name="GetCodesProducedByGroupResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="BatchValidationsLogResponse">
    <wsdl:part element="tns:BatchValidationsLogResponse" name="BatchValidationsLogResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ApplyAtiTemplateGroupResponse">
    <wsdl:part element="tns:ApplyAtiTemplateGroupResponse" name="ApplyAtiTemplateGroupResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AddAtiGroupRequest">
    <wsdl:part element="tns:AddAtiGroupRequest" name="AddAtiGroupRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="SetCodeStatusResponse">
    <wsdl:part element="tns:SetCodeStatusResponse" name="SetCodeStatusResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DiskUsageRequest">
    <wsdl:part element="tns:DiskUsageRequest" name="DiskUsageRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeBlacklistRequest">
    <wsdl:part element="tns:CodeBlacklistRequest" name="CodeBlacklistRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListOrdersRequest">
    <wsdl:part element="tns:ListOrdersRequest" name="ListOrdersRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListAllExpansionsResponse">
    <wsdl:part element="tns:ListAllExpansionsResponse" name="ListAllExpansionsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateCodeStatusConfigResponse">
    <wsdl:part element="tns:UpdateCodeStatusConfigResponse" name="UpdateCodeStatusConfigResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateEntryChannelTranslationsResponse">
    <wsdl:part element="tns:UpdateEntryChannelTranslationsResponse" name="UpdateEntryChannelTranslationsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="WorkersInfoRequest">
    <wsdl:part element="tns:WorkersInfoRequest" name="WorkersInfoRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="StatisticsLastOrderedExpansionsResponse">
    <wsdl:part element="tns:StatisticsLastOrderedExpansionsResponse" name="StatisticsLastOrderedExpansionsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodeStatusConfigRequest">
    <wsdl:part element="tns:GetCodeStatusConfigRequest" name="GetCodeStatusConfigRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteProductMetadataSchemaRequest">
    <wsdl:part element="tns:DeleteProductMetadataSchemaRequest" name="DeleteProductMetadataSchemaRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="SetDefaultMetadataSchemaRequest">
    <wsdl:part element="tns:SetDefaultMetadataSchemaRequest" name="SetDefaultMetadataSchemaRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteLastExpansionRequest">
    <wsdl:part element="tns:DeleteLastExpansionRequest" name="DeleteLastExpansionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListOrdersResponse">
    <wsdl:part element="tns:ListOrdersResponse" name="ListOrdersResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CalibrateRollResponse">
    <wsdl:part element="tns:CalibrateRollResponse" name="CalibrateRollResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetOrderValidationsResponse">
    <wsdl:part element="tns:GetOrderValidationsResponse" name="GetOrderValidationsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadSectionRequest">
    <wsdl:part element="tns:ReadSectionRequest" name="ReadSectionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetEntryChannelRequest">
    <wsdl:part element="tns:GetEntryChannelRequest" name="GetEntryChannelRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DefaultAtiGroupRequest">
    <wsdl:part element="tns:DefaultAtiGroupRequest" name="DefaultAtiGroupRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateSectionRequest">
    <wsdl:part element="tns:CreateSectionRequest" name="CreateSectionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AddAtiRequest">
    <wsdl:part element="tns:AddAtiRequest" name="AddAtiRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteReservedSsccSequenceResponse">
    <wsdl:part element="tns:DeleteReservedSsccSequenceResponse" name="DeleteReservedSsccSequenceResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AddReservedSsccSequenceResponse">
    <wsdl:part element="tns:AddReservedSsccSequenceResponse" name="AddReservedSsccSequenceResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListProductsResponse">
    <wsdl:part element="tns:ListProductsResponse" name="ListProductsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AddCodeStatusConfigResponse">
    <wsdl:part element="tns:AddCodeStatusConfigResponse" name="AddCodeStatusConfigResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="StatisticsLastOrdersRequest">
    <wsdl:part element="tns:StatisticsLastOrdersRequest" name="StatisticsLastOrdersRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="FindLookAlikeCodeRequest">
    <wsdl:part element="tns:FindLookAlikeCodeRequest" name="FindLookAlikeCodeRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="SetExpansionStatusResponse">
    <wsdl:part element="tns:SetExpansionStatusResponse" name="SetExpansionStatusResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateProductResponse">
    <wsdl:part element="tns:UpdateProductResponse" name="UpdateProductResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetOrderExpansionsValidationsResponse">
    <wsdl:part element="tns:GetOrderExpansionsValidationsResponse" name="GetOrderExpansionsValidationsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListSectionAtisRequest">
    <wsdl:part element="tns:ListSectionAtisRequest" name="ListSectionAtisRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="StatisticsLastProducedExpansionsResponse">
    <wsdl:part element="tns:StatisticsLastProducedExpansionsResponse" name="StatisticsLastProducedExpansionsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteLastExpansionResponse">
    <wsdl:part element="tns:DeleteLastExpansionResponse" name="DeleteLastExpansionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UnlinkAtiRequest">
    <wsdl:part element="tns:UnlinkAtiRequest" name="UnlinkAtiRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListCodeConfigsRequest">
    <wsdl:part element="tns:ListCodeConfigsRequest" name="ListCodeConfigsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeactivateSectionRequest">
    <wsdl:part element="tns:DeactivateSectionRequest" name="DeactivateSectionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UnlinkAllAtisRequest">
    <wsdl:part element="tns:UnlinkAllAtisRequest" name="UnlinkAllAtisRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeActivateSectionInRollRequest">
    <wsdl:part element="tns:DeActivateSectionInRollRequest" name="DeActivateSectionInRollRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetOrderCodeStatusStatisticsResponse">
    <wsdl:part element="tns:GetOrderCodeStatusStatisticsResponse" name="GetOrderCodeStatusStatisticsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DownloadCodesRequest">
    <wsdl:part element="tns:DownloadCodesRequest" name="DownloadCodesRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetProductRequest">
    <wsdl:part element="tns:GetProductRequest" name="GetProductRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListCodePatternsRequest">
    <wsdl:part element="tns:ListCodePatternsRequest" name="ListCodePatternsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListSectionsResponse">
    <wsdl:part element="tns:ListSectionsResponse" name="ListSectionsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AddAtiGroupResponse">
    <wsdl:part element="tns:AddAtiGroupResponse" name="AddAtiGroupResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateNewSectionInRollResponse">
    <wsdl:part element="tns:CreateNewSectionInRollResponse" name="CreateNewSectionInRollResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UnlinkAllAtisResponse">
    <wsdl:part element="tns:UnlinkAllAtisResponse" name="UnlinkAllAtisResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodesProducedByProductRequest">
    <wsdl:part element="tns:GetCodesProducedByProductRequest" name="GetCodesProducedByProductRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListAtiGroupsResponse">
    <wsdl:part element="tns:ListAtiGroupsResponse" name="ListAtiGroupsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ValidationsLogFilterRequest">
    <wsdl:part element="tns:ValidationsLogFilterRequest" name="ValidationsLogFilterRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateOrderSectionMetadataResponse">
    <wsdl:part element="tns:UpdateOrderSectionMetadataResponse" name="UpdateOrderSectionMetadataResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetOrderValidationsRequest">
    <wsdl:part element="tns:GetOrderValidationsRequest" name="GetOrderValidationsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteEntryChannelRequest">
    <wsdl:part element="tns:DeleteEntryChannelRequest" name="DeleteEntryChannelRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeActivateSectionInRollResponse">
    <wsdl:part element="tns:DeActivateSectionInRollResponse" name="DeActivateSectionInRollResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateOrderMetadataRequest">
    <wsdl:part element="tns:UpdateOrderMetadataRequest" name="UpdateOrderMetadataRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="WorkersInfoResponse">
    <wsdl:part element="tns:WorkersInfoResponse" name="WorkersInfoResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListAllExpansionsRequest">
    <wsdl:part element="tns:ListAllExpansionsRequest" name="ListAllExpansionsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="BatchValidationsLogRequest">
    <wsdl:part element="tns:BatchValidationsLogRequest" name="BatchValidationsLogRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteProductMetadataSchemaResponse">
    <wsdl:part element="tns:DeleteProductMetadataSchemaResponse" name="DeleteProductMetadataSchemaResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetOrderCodeStatusStatisticsRequest">
    <wsdl:part element="tns:GetOrderCodeStatusStatisticsRequest" name="GetOrderCodeStatusStatisticsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodesProducedByUserResponse">
    <wsdl:part element="tns:GetCodesProducedByUserResponse" name="GetCodesProducedByUserResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodeStatusChangesRequest">
    <wsdl:part element="tns:GetCodeStatusChangesRequest" name="GetCodeStatusChangesRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateAtiRequest">
    <wsdl:part element="tns:UpdateAtiRequest" name="UpdateAtiRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListAtisRequest">
    <wsdl:part element="tns:ListAtisRequest" name="ListAtisRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListProductsRequest">
    <wsdl:part element="tns:ListProductsRequest" name="ListProductsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateCodeStatusConfigRequest">
    <wsdl:part element="tns:UpdateCodeStatusConfigRequest" name="UpdateCodeStatusConfigRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeValidatorResponse">
    <wsdl:part element="tns:CodeValidatorResponse" name="CodeValidatorResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeDissectorResponse">
    <wsdl:part element="tns:CodeDissectorResponse" name="CodeDissectorResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AppCodeValidatorResponse">
    <wsdl:part element="tns:AppCodeValidatorResponse" name="AppCodeValidatorResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CustomerCodeDissectorRequest">
    <wsdl:part element="tns:CustomerCodeDissectorRequest" name="CustomerCodeDissectorRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetRollResponse">
    <wsdl:part element="tns:GetRollResponse" name="GetRollResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="SetCodeStatusForOrderRequest">
    <wsdl:part element="tns:SetCodeStatusForOrderRequest" name="SetCodeStatusForOrderRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ApplyAtiGroupResponse">
    <wsdl:part element="tns:ApplyAtiGroupResponse" name="ApplyAtiGroupResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeactivateSectionResponse">
    <wsdl:part element="tns:DeactivateSectionResponse" name="DeactivateSectionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeValidatorRequest">
    <wsdl:part element="tns:CodeValidatorRequest" name="CodeValidatorRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="LockOrderRequest">
    <wsdl:part element="tns:LockOrderRequest" name="LockOrderRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateEntryChannelRequest">
    <wsdl:part element="tns:UpdateEntryChannelRequest" name="UpdateEntryChannelRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AddAtiResponse">
    <wsdl:part element="tns:AddAtiResponse" name="AddAtiResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="StatisticsResponse">
    <wsdl:part element="tns:StatisticsResponse" name="StatisticsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="FindLookAlikeCodeResponse">
    <wsdl:part element="tns:FindLookAlikeCodeResponse" name="FindLookAlikeCodeResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="IPLocalizationResponse">
    <wsdl:part element="tns:IPLocalizationResponse" name="IPLocalizationResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ExpansionsStatusRequest">
    <wsdl:part element="tns:ExpansionsStatusRequest" name="ExpansionsStatusRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeBlacklistRemoveRequest">
    <wsdl:part element="tns:CodeBlacklistRemoveRequest" name="CodeBlacklistRemoveRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodesProducedByProductResponse">
    <wsdl:part element="tns:GetCodesProducedByProductResponse" name="GetCodesProducedByProductResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeBlacklistResponse">
    <wsdl:part element="tns:CodeBlacklistResponse" name="CodeBlacklistResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="SetCodeStatusForOrderResponse">
    <wsdl:part element="tns:SetCodeStatusForOrderResponse" name="SetCodeStatusForOrderResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteMetadataSchemaRequest">
    <wsdl:part element="tns:DeleteMetadataSchemaRequest" name="DeleteMetadataSchemaRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteOrderSectionMetadataResponse">
    <wsdl:part element="tns:DeleteOrderSectionMetadataResponse" name="DeleteOrderSectionMetadataResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ExpansionsInfoRequest">
    <wsdl:part element="tns:ExpansionsInfoRequest" name="ExpansionsInfoRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListExpansionsRequest">
    <wsdl:part element="tns:ListExpansionsRequest" name="ListExpansionsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadRollResponse">
    <wsdl:part element="tns:ReadRollResponse" name="ReadRollResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodeStatusHistoryRequest">
    <wsdl:part element="tns:GetCodeStatusHistoryRequest" name="GetCodeStatusHistoryRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeBlacklistAddRequest">
    <wsdl:part element="tns:CodeBlacklistAddRequest" name="CodeBlacklistAddRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateSectionResponse">
    <wsdl:part element="tns:UpdateSectionResponse" name="UpdateSectionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="SetCodeStatusRequest">
    <wsdl:part element="tns:SetCodeStatusRequest" name="SetCodeStatusRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateProductRequest">
    <wsdl:part element="tns:CreateProductRequest" name="CreateProductRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateAtiGroupRequest">
    <wsdl:part element="tns:UpdateAtiGroupRequest" name="UpdateAtiGroupRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ActivateRollSectionRequest">
    <wsdl:part element="tns:ActivateRollSectionRequest" name="ActivateRollSectionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateOrderDataRequest">
    <wsdl:part element="tns:UpdateOrderDataRequest" name="UpdateOrderDataRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ExpandOrderRequest">
    <wsdl:part element="tns:ExpandOrderRequest" name="ExpandOrderRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="RenameAtiRequest">
    <wsdl:part element="tns:RenameAtiRequest" name="RenameAtiRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateCodeConfigRequest">
    <wsdl:part element="tns:CreateCodeConfigRequest" name="CreateCodeConfigRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="StatisticsLastOrderedExpansionsRequest">
    <wsdl:part element="tns:StatisticsLastOrderedExpansionsRequest" name="StatisticsLastOrderedExpansionsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListEntryChannelsRequest">
    <wsdl:part element="tns:ListEntryChannelsRequest" name="ListEntryChannelsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetProductResponse">
    <wsdl:part element="tns:GetProductResponse" name="GetProductResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ApplyAtiRequest">
    <wsdl:part element="tns:ApplyAtiRequest" name="ApplyAtiRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="SetDefaultMetadataSchemaResponse">
    <wsdl:part element="tns:SetDefaultMetadataSchemaResponse" name="SetDefaultMetadataSchemaResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadOrderRequest">
    <wsdl:part element="tns:ReadOrderRequest" name="ReadOrderRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="RenameAtiResponse">
    <wsdl:part element="tns:RenameAtiResponse" name="RenameAtiResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DefaultAtiGroupResponse">
    <wsdl:part element="tns:DefaultAtiGroupResponse" name="DefaultAtiGroupResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetExpansionResponse">
    <wsdl:part element="tns:GetExpansionResponse" name="GetExpansionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeBlacklistRemoveResponse">
    <wsdl:part element="tns:CodeBlacklistRemoveResponse" name="CodeBlacklistRemoveResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateOrderResponse">
    <wsdl:part element="tns:UpdateOrderResponse" name="UpdateOrderResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteAtiRequest">
    <wsdl:part element="tns:DeleteAtiRequest" name="DeleteAtiRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateEntryChannelRequest">
    <wsdl:part element="tns:CreateEntryChannelRequest" name="CreateEntryChannelRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateOrderMetadataResponse">
    <wsdl:part element="tns:UpdateOrderMetadataResponse" name="UpdateOrderMetadataResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ApplyAtiResponse">
    <wsdl:part element="tns:ApplyAtiResponse" name="ApplyAtiResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="MapExpansionsToSectionsResponse">
    <wsdl:part element="tns:MapExpansionsToSectionsResponse" name="MapExpansionsToSectionsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CalibrateRollRequest">
    <wsdl:part element="tns:CalibrateRollRequest" name="CalibrateRollRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadAtiRequest">
    <wsdl:part element="tns:ReadAtiRequest" name="ReadAtiRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateCodeConfigResponse">
    <wsdl:part element="tns:CreateCodeConfigResponse" name="CreateCodeConfigResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadAtiGroupRequest">
    <wsdl:part element="tns:ReadAtiGroupRequest" name="ReadAtiGroupRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateOrderSectionMetadataRequest">
    <wsdl:part element="tns:UpdateOrderSectionMetadataRequest" name="UpdateOrderSectionMetadataRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="BatchCodeValidatorRequest">
    <wsdl:part element="tns:BatchCodeValidatorRequest" name="BatchCodeValidatorRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="IPLocalizationRequest">
    <wsdl:part element="tns:IPLocalizationRequest" name="IPLocalizationRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DownloadCodesResponse">
    <wsdl:part element="tns:DownloadCodesResponse" name="DownloadCodesResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="BatchCodeValidatorResponse">
    <wsdl:part element="tns:BatchCodeValidatorResponse" name="BatchCodeValidatorResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="StatisticsRequest">
    <wsdl:part element="tns:StatisticsRequest" name="StatisticsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteMetadataSchemaResponse">
    <wsdl:part element="tns:DeleteMetadataSchemaResponse" name="DeleteMetadataSchemaResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadRollRequest">
    <wsdl:part element="tns:ReadRollRequest" name="ReadRollRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="InitOrderRequest">
    <wsdl:part element="tns:InitOrderRequest" name="InitOrderRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateSsccSequenceResponse">
    <wsdl:part element="tns:CreateSsccSequenceResponse" name="CreateSsccSequenceResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteSectionRequest">
    <wsdl:part element="tns:DeleteSectionRequest" name="DeleteSectionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="StatisticsLastProducedExpansionsRequest">
    <wsdl:part element="tns:StatisticsLastProducedExpansionsRequest" name="StatisticsLastProducedExpansionsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UnlinkAtiResponse">
    <wsdl:part element="tns:UnlinkAtiResponse" name="UnlinkAtiResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListCodePatternsResponse">
    <wsdl:part element="tns:ListCodePatternsResponse" name="ListCodePatternsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadSsccSequenceRequest">
    <wsdl:part element="tns:ReadSsccSequenceRequest" name="ReadSsccSequenceRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetExpansionRequest">
    <wsdl:part element="tns:GetExpansionRequest" name="GetExpansionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateEntryChannelTranslationsRequest">
    <wsdl:part element="tns:UpdateEntryChannelTranslationsRequest" name="UpdateEntryChannelTranslationsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateOrderRequest">
    <wsdl:part element="tns:UpdateOrderRequest" name="UpdateOrderRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="InitOrderResponse">
    <wsdl:part element="tns:InitOrderResponse" name="InitOrderResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="MapExpansionsToSectionsRequest">
    <wsdl:part element="tns:MapExpansionsToSectionsRequest" name="MapExpansionsToSectionsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetOrderExpansionsValidationsRequest">
    <wsdl:part element="tns:GetOrderExpansionsValidationsRequest" name="GetOrderExpansionsValidationsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="IdentifyRollRequest">
    <wsdl:part element="tns:IdentifyRollRequest" name="IdentifyRollRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AddCodeStatusConfigRequest">
    <wsdl:part element="tns:AddCodeStatusConfigRequest" name="AddCodeStatusConfigRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteAtiGroupRequest">
    <wsdl:part element="tns:DeleteAtiGroupRequest" name="DeleteAtiGroupRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ApplyAtiGroupRequest">
    <wsdl:part element="tns:ApplyAtiGroupRequest" name="ApplyAtiGroupRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListMetadataSchemasRequest">
    <wsdl:part element="tns:ListMetadataSchemasRequest" name="ListMetadataSchemasRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadCodeStatusConfigResponse">
    <wsdl:part element="tns:ReadCodeStatusConfigResponse" name="ReadCodeStatusConfigResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListReservedSsccSequenceRequest">
    <wsdl:part element="tns:ListReservedSsccSequenceRequest" name="ListReservedSsccSequenceRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateOrderDataResponse">
    <wsdl:part element="tns:UpdateOrderDataResponse" name="UpdateOrderDataResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadOrderSectionMetadataRequest">
    <wsdl:part element="tns:ReadOrderSectionMetadataRequest" name="ReadOrderSectionMetadataRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListMetadataSchemasResponse">
    <wsdl:part element="tns:ListMetadataSchemasResponse" name="ListMetadataSchemasResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadOrderResponse">
    <wsdl:part element="tns:ReadOrderResponse" name="ReadOrderResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="LockOrderResponse">
    <wsdl:part element="tns:LockOrderResponse" name="LockOrderResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="IdentifyRollResponse">
    <wsdl:part element="tns:IdentifyRollResponse" name="IdentifyRollResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListCodeConfigsResponse">
    <wsdl:part element="tns:ListCodeConfigsResponse" name="ListCodeConfigsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadOrderSectionMetadataResponse">
    <wsdl:part element="tns:ReadOrderSectionMetadataResponse" name="ReadOrderSectionMetadataResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetOrderSectionsValidationsRequest">
    <wsdl:part element="tns:GetOrderSectionsValidationsRequest" name="GetOrderSectionsValidationsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListProductMetadataSchemasRequest">
    <wsdl:part element="tns:ListProductMetadataSchemasRequest" name="ListProductMetadataSchemasRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="StatisticsLastOrdersResponse">
    <wsdl:part element="tns:StatisticsLastOrdersResponse" name="StatisticsLastOrdersResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListSectionAtisResponse">
    <wsdl:part element="tns:ListSectionAtisResponse" name="ListSectionAtisResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListEntryChannelsResponse">
    <wsdl:part element="tns:ListEntryChannelsResponse" name="ListEntryChannelsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ExpansionsStatusResponse">
    <wsdl:part element="tns:ExpansionsStatusResponse" name="ExpansionsStatusResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="BatchValidationDetailsRequest">
    <wsdl:part element="tns:BatchValidationDetailsRequest" name="BatchValidationDetailsRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateAtiResponse">
    <wsdl:part element="tns:UpdateAtiResponse" name="UpdateAtiResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListProductMetadataSchemasResponse">
    <wsdl:part element="tns:ListProductMetadataSchemasResponse" name="ListProductMetadataSchemasResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="MarkTemporaryRollEndRequest">
    <wsdl:part element="tns:MarkTemporaryRollEndRequest" name="MarkTemporaryRollEndRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteSectionResponse">
    <wsdl:part element="tns:DeleteSectionResponse" name="DeleteSectionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodeStatusChangesResponse">
    <wsdl:part element="tns:GetCodeStatusChangesResponse" name="GetCodeStatusChangesResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteOrderMetadataResponse">
    <wsdl:part element="tns:DeleteOrderMetadataResponse" name="DeleteOrderMetadataResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListExpansionsResponse">
    <wsdl:part element="tns:ListExpansionsResponse" name="ListExpansionsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CodeDissectorRequest">
    <wsdl:part element="tns:CodeDissectorRequest" name="CodeDissectorRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateSsccSequenceRequest">
    <wsdl:part element="tns:CreateSsccSequenceRequest" name="CreateSsccSequenceRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadSsccRequest">
    <wsdl:part element="tns:ReadSsccRequest" name="ReadSsccRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateProductRequest">
    <wsdl:part element="tns:UpdateProductRequest" name="UpdateProductRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadAtiGroupResponse">
    <wsdl:part element="tns:ReadAtiGroupResponse" name="ReadAtiGroupResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DiskUsageResponse">
    <wsdl:part element="tns:DiskUsageResponse" name="DiskUsageResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetRollRequest">
    <wsdl:part element="tns:GetRollRequest" name="GetRollRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AddReservedSsccSequenceRequest">
    <wsdl:part element="tns:AddReservedSsccSequenceRequest" name="AddReservedSsccSequenceRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListExpansionCodesRequest">
    <wsdl:part element="tns:ListExpansionCodesRequest" name="ListExpansionCodesRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="AppCodeValidatorRequest">
    <wsdl:part element="tns:AppCodeValidatorRequest" name="AppCodeValidatorRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodeResponse">
    <wsdl:part element="tns:GetCodeResponse" name="GetCodeResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateSectionResponse">
    <wsdl:part element="tns:CreateSectionResponse" name="CreateSectionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteAtiResponse">
    <wsdl:part element="tns:DeleteAtiResponse" name="DeleteAtiResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ListReservedSsccSequenceResponse">
    <wsdl:part element="tns:ListReservedSsccSequenceResponse" name="ListReservedSsccSequenceResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteProductResponse">
    <wsdl:part element="tns:DeleteProductResponse" name="DeleteProductResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateSectionRequest">
    <wsdl:part element="tns:UpdateSectionRequest" name="UpdateSectionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadOrderMetadataRequest">
    <wsdl:part element="tns:ReadOrderMetadataRequest" name="ReadOrderMetadataRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodesProducedByUserRequest">
    <wsdl:part element="tns:GetCodesProducedByUserRequest" name="GetCodesProducedByUserRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteOrderMetadataRequest">
    <wsdl:part element="tns:DeleteOrderMetadataRequest" name="DeleteOrderMetadataRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ActivateSectionResponse">
    <wsdl:part element="tns:ActivateSectionResponse" name="ActivateSectionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="MarkTemporaryRollEndResponse">
    <wsdl:part element="tns:MarkTemporaryRollEndResponse" name="MarkTemporaryRollEndResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadOrderMetadataResponse">
    <wsdl:part element="tns:ReadOrderMetadataResponse" name="ReadOrderMetadataResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CustomerCodeDissectorResponse">
    <wsdl:part element="tns:CustomerCodeDissectorResponse" name="CustomerCodeDissectorResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ValidationsLogFilterResponse">
    <wsdl:part element="tns:ValidationsLogFilterResponse" name="ValidationsLogFilterResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetEntryChannelResponse">
    <wsdl:part element="tns:GetEntryChannelResponse" name="GetEntryChannelResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="CreateNewSectionInRollRequest">
    <wsdl:part element="tns:CreateNewSectionInRollRequest" name="CreateNewSectionInRollRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="SetExpansionStatusRequest">
    <wsdl:part element="tns:SetExpansionStatusRequest" name="SetExpansionStatusRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteReservedSsccSequenceRequest">
    <wsdl:part element="tns:DeleteReservedSsccSequenceRequest" name="DeleteReservedSsccSequenceRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteEntryChannelResponse">
    <wsdl:part element="tns:DeleteEntryChannelResponse" name="DeleteEntryChannelResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodeStatusConfigResponse">
    <wsdl:part element="tns:GetCodeStatusConfigResponse" name="GetCodeStatusConfigResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadSectionResponse">
    <wsdl:part element="tns:ReadSectionResponse" name="ReadSectionResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="GetCodeStatusHistoryResponse">
    <wsdl:part element="tns:GetCodeStatusHistoryResponse" name="GetCodeStatusHistoryResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteAtiGroupResponse">
    <wsdl:part element="tns:DeleteAtiGroupResponse" name="DeleteAtiGroupResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="BatchValidationDetailsResponse">
    <wsdl:part element="tns:BatchValidationDetailsResponse" name="BatchValidationDetailsResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteOrderSectionMetadataRequest">
    <wsdl:part element="tns:DeleteOrderSectionMetadataRequest" name="DeleteOrderSectionMetadataRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ReadSsccSequenceResponse">
    <wsdl:part element="tns:ReadSsccSequenceResponse" name="ReadSsccSequenceResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ExpansionsInfoResponse">
    <wsdl:part element="tns:ExpansionsInfoResponse" name="ExpansionsInfoResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="MultiExpandOrderRequest">
    <wsdl:part element="tns:MultiExpandOrderRequest" name="MultiExpandOrderRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="ActivateSectionRequest">
    <wsdl:part element="tns:ActivateSectionRequest" name="ActivateSectionRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="DeleteProductRequest">
    <wsdl:part element="tns:DeleteProductRequest" name="DeleteProductRequest">
    </wsdl:part>
  </wsdl:message>
  <wsdl:message name="UpdateEntryChannelResponse">
    <wsdl:part element="tns:UpdateEntryChannelResponse" name="UpdateEntryChannelResponse">
    </wsdl:part>
  </wsdl:message>
  <wsdl:portType name="kcengine">
    <wsdl:operation name="ApplyAtiTemplateGroup">
      <wsdl:input message="tns:ApplyAtiTemplateGroupRequest" name="ApplyAtiTemplateGroupRequest">
    </wsdl:input>
      <wsdl:output message="tns:ApplyAtiTemplateGroupResponse" name="ApplyAtiTemplateGroupResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateEntryChannel">
      <wsdl:input message="tns:CreateEntryChannelRequest" name="CreateEntryChannelRequest">
    </wsdl:input>
      <wsdl:output message="tns:CreateEntryChannelResponse" name="CreateEntryChannelResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadCodeConfig">
      <wsdl:input message="tns:ReadCodeConfigRequest" name="ReadCodeConfigRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadCodeConfigResponse" name="ReadCodeConfigResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListSections">
      <wsdl:input message="tns:ListSectionsRequest" name="ListSectionsRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListSectionsResponse" name="ListSectionsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetOrderSectionsValidations">
      <wsdl:input message="tns:GetOrderSectionsValidationsRequest" name="GetOrderSectionsValidationsRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetOrderSectionsValidationsResponse" name="GetOrderSectionsValidationsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ActivateRollSection">
      <wsdl:input message="tns:ActivateRollSectionRequest" name="ActivateRollSectionRequest">
    </wsdl:input>
      <wsdl:output message="tns:ActivateRollSectionResponse" name="ActivateRollSectionResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateProduct">
      <wsdl:input message="tns:CreateProductRequest" name="CreateProductRequest">
    </wsdl:input>
      <wsdl:output message="tns:CreateProductResponse" name="CreateProductResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCode">
      <wsdl:input message="tns:GetCodeRequest" name="GetCodeRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetCodeResponse" name="GetCodeResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadSscc">
      <wsdl:input message="tns:ReadSsccRequest" name="ReadSsccRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadSsccResponse" name="ReadSsccResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="MultiExpandOrder">
      <wsdl:input message="tns:MultiExpandOrderRequest" name="MultiExpandOrderRequest">
    </wsdl:input>
      <wsdl:output message="tns:MultiExpandOrderResponse" name="MultiExpandOrderResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadAti">
      <wsdl:input message="tns:ReadAtiRequest" name="ReadAtiRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadAtiResponse" name="ReadAtiResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeBlacklistAdd">
      <wsdl:input message="tns:CodeBlacklistAddRequest" name="CodeBlacklistAddRequest">
    </wsdl:input>
      <wsdl:output message="tns:CodeBlacklistAddResponse" name="CodeBlacklistAddResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadCodeStatusConfig">
      <wsdl:input message="tns:ReadCodeStatusConfigRequest" name="ReadCodeStatusConfigRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadCodeStatusConfigResponse" name="ReadCodeStatusConfigResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListExpansionCodes">
      <wsdl:input message="tns:ListExpansionCodesRequest" name="ListExpansionCodesRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListExpansionCodesResponse" name="ListExpansionCodesResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListAtis">
      <wsdl:input message="tns:ListAtisRequest" name="ListAtisRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListAtisResponse" name="ListAtisResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListAtiGroups">
      <wsdl:input message="tns:ListAtiGroupsRequest" name="ListAtiGroupsRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListAtiGroupsResponse" name="ListAtiGroupsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateAtiGroup">
      <wsdl:input message="tns:UpdateAtiGroupRequest" name="UpdateAtiGroupRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateAtiGroupResponse" name="UpdateAtiGroupResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ExpandOrder">
      <wsdl:input message="tns:ExpandOrderRequest" name="ExpandOrderRequest">
    </wsdl:input>
      <wsdl:output message="tns:ExpandOrderResponse" name="ExpandOrderResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodesProducedByGroup">
      <wsdl:input message="tns:GetCodesProducedByGroupRequest" name="GetCodesProducedByGroupRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetCodesProducedByGroupResponse" name="GetCodesProducedByGroupResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="BatchValidationsLog">
      <wsdl:input message="tns:BatchValidationsLogRequest" name="BatchValidationsLogRequest">
    </wsdl:input>
      <wsdl:output message="tns:BatchValidationsLogResponse" name="BatchValidationsLogResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AddAtiGroup">
      <wsdl:input message="tns:AddAtiGroupRequest" name="AddAtiGroupRequest">
    </wsdl:input>
      <wsdl:output message="tns:AddAtiGroupResponse" name="AddAtiGroupResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="SetCodeStatus">
      <wsdl:input message="tns:SetCodeStatusRequest" name="SetCodeStatusRequest">
    </wsdl:input>
      <wsdl:output message="tns:SetCodeStatusResponse" name="SetCodeStatusResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DiskUsage">
      <wsdl:input message="tns:DiskUsageRequest" name="DiskUsageRequest">
    </wsdl:input>
      <wsdl:output message="tns:DiskUsageResponse" name="DiskUsageResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeBlacklist">
      <wsdl:input message="tns:CodeBlacklistRequest" name="CodeBlacklistRequest">
    </wsdl:input>
      <wsdl:output message="tns:CodeBlacklistResponse" name="CodeBlacklistResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListOrders">
      <wsdl:input message="tns:ListOrdersRequest" name="ListOrdersRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListOrdersResponse" name="ListOrdersResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListAllExpansions">
      <wsdl:input message="tns:ListAllExpansionsRequest" name="ListAllExpansionsRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListAllExpansionsResponse" name="ListAllExpansionsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateCodeStatusConfig">
      <wsdl:input message="tns:UpdateCodeStatusConfigRequest" name="UpdateCodeStatusConfigRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateCodeStatusConfigResponse" name="UpdateCodeStatusConfigResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateEntryChannelTranslations">
      <wsdl:input message="tns:UpdateEntryChannelTranslationsRequest" name="UpdateEntryChannelTranslationsRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateEntryChannelTranslationsResponse" name="UpdateEntryChannelTranslationsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="WorkersInfo">
      <wsdl:input message="tns:WorkersInfoRequest" name="WorkersInfoRequest">
    </wsdl:input>
      <wsdl:output message="tns:WorkersInfoResponse" name="WorkersInfoResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="StatisticsLastOrderedExpansions">
      <wsdl:input message="tns:StatisticsLastOrderedExpansionsRequest" name="StatisticsLastOrderedExpansionsRequest">
    </wsdl:input>
      <wsdl:output message="tns:StatisticsLastOrderedExpansionsResponse" name="StatisticsLastOrderedExpansionsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodeStatusConfig">
      <wsdl:input message="tns:GetCodeStatusConfigRequest" name="GetCodeStatusConfigRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetCodeStatusConfigResponse" name="GetCodeStatusConfigResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteProductMetadataSchema">
      <wsdl:input message="tns:DeleteProductMetadataSchemaRequest" name="DeleteProductMetadataSchemaRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteProductMetadataSchemaResponse" name="DeleteProductMetadataSchemaResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="SetDefaultMetadataSchema">
      <wsdl:input message="tns:SetDefaultMetadataSchemaRequest" name="SetDefaultMetadataSchemaRequest">
    </wsdl:input>
      <wsdl:output message="tns:SetDefaultMetadataSchemaResponse" name="SetDefaultMetadataSchemaResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteLastExpansion">
      <wsdl:input message="tns:DeleteLastExpansionRequest" name="DeleteLastExpansionRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteLastExpansionResponse" name="DeleteLastExpansionResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CalibrateRoll">
      <wsdl:input message="tns:CalibrateRollRequest" name="CalibrateRollRequest">
    </wsdl:input>
      <wsdl:output message="tns:CalibrateRollResponse" name="CalibrateRollResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetOrderValidations">
      <wsdl:input message="tns:GetOrderValidationsRequest" name="GetOrderValidationsRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetOrderValidationsResponse" name="GetOrderValidationsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadSection">
      <wsdl:input message="tns:ReadSectionRequest" name="ReadSectionRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadSectionResponse" name="ReadSectionResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetEntryChannel">
      <wsdl:input message="tns:GetEntryChannelRequest" name="GetEntryChannelRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetEntryChannelResponse" name="GetEntryChannelResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DefaultAtiGroup">
      <wsdl:input message="tns:DefaultAtiGroupRequest" name="DefaultAtiGroupRequest">
    </wsdl:input>
      <wsdl:output message="tns:DefaultAtiGroupResponse" name="DefaultAtiGroupResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateSection">
      <wsdl:input message="tns:CreateSectionRequest" name="CreateSectionRequest">
    </wsdl:input>
      <wsdl:output message="tns:CreateSectionResponse" name="CreateSectionResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AddAti">
      <wsdl:input message="tns:AddAtiRequest" name="AddAtiRequest">
    </wsdl:input>
      <wsdl:output message="tns:AddAtiResponse" name="AddAtiResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteReservedSsccSequence">
      <wsdl:input message="tns:DeleteReservedSsccSequenceRequest" name="DeleteReservedSsccSequenceRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteReservedSsccSequenceResponse" name="DeleteReservedSsccSequenceResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AddReservedSsccSequence">
      <wsdl:input message="tns:AddReservedSsccSequenceRequest" name="AddReservedSsccSequenceRequest">
    </wsdl:input>
      <wsdl:output message="tns:AddReservedSsccSequenceResponse" name="AddReservedSsccSequenceResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListProducts">
      <wsdl:input message="tns:ListProductsRequest" name="ListProductsRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListProductsResponse" name="ListProductsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AddCodeStatusConfig">
      <wsdl:input message="tns:AddCodeStatusConfigRequest" name="AddCodeStatusConfigRequest">
    </wsdl:input>
      <wsdl:output message="tns:AddCodeStatusConfigResponse" name="AddCodeStatusConfigResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="StatisticsLastOrders">
      <wsdl:input message="tns:StatisticsLastOrdersRequest" name="StatisticsLastOrdersRequest">
    </wsdl:input>
      <wsdl:output message="tns:StatisticsLastOrdersResponse" name="StatisticsLastOrdersResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="FindLookAlikeCode">
      <wsdl:input message="tns:FindLookAlikeCodeRequest" name="FindLookAlikeCodeRequest">
    </wsdl:input>
      <wsdl:output message="tns:FindLookAlikeCodeResponse" name="FindLookAlikeCodeResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="SetExpansionStatus">
      <wsdl:input message="tns:SetExpansionStatusRequest" name="SetExpansionStatusRequest">
    </wsdl:input>
      <wsdl:output message="tns:SetExpansionStatusResponse" name="SetExpansionStatusResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateProduct">
      <wsdl:input message="tns:UpdateProductRequest" name="UpdateProductRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateProductResponse" name="UpdateProductResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetOrderExpansionsValidations">
      <wsdl:input message="tns:GetOrderExpansionsValidationsRequest" name="GetOrderExpansionsValidationsRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetOrderExpansionsValidationsResponse" name="GetOrderExpansionsValidationsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListSectionAtis">
      <wsdl:input message="tns:ListSectionAtisRequest" name="ListSectionAtisRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListSectionAtisResponse" name="ListSectionAtisResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="StatisticsLastProducedExpansions">
      <wsdl:input message="tns:StatisticsLastProducedExpansionsRequest" name="StatisticsLastProducedExpansionsRequest">
    </wsdl:input>
      <wsdl:output message="tns:StatisticsLastProducedExpansionsResponse" name="StatisticsLastProducedExpansionsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UnlinkAti">
      <wsdl:input message="tns:UnlinkAtiRequest" name="UnlinkAtiRequest">
    </wsdl:input>
      <wsdl:output message="tns:UnlinkAtiResponse" name="UnlinkAtiResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListCodeConfigs">
      <wsdl:input message="tns:ListCodeConfigsRequest" name="ListCodeConfigsRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListCodeConfigsResponse" name="ListCodeConfigsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeactivateSection">
      <wsdl:input message="tns:DeactivateSectionRequest" name="DeactivateSectionRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeactivateSectionResponse" name="DeactivateSectionResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UnlinkAllAtis">
      <wsdl:input message="tns:UnlinkAllAtisRequest" name="UnlinkAllAtisRequest">
    </wsdl:input>
      <wsdl:output message="tns:UnlinkAllAtisResponse" name="UnlinkAllAtisResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeActivateSectionInRoll">
      <wsdl:input message="tns:DeActivateSectionInRollRequest" name="DeActivateSectionInRollRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeActivateSectionInRollResponse" name="DeActivateSectionInRollResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetOrderCodeStatusStatistics">
      <wsdl:input message="tns:GetOrderCodeStatusStatisticsRequest" name="GetOrderCodeStatusStatisticsRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetOrderCodeStatusStatisticsResponse" name="GetOrderCodeStatusStatisticsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DownloadCodes">
      <wsdl:input message="tns:DownloadCodesRequest" name="DownloadCodesRequest">
    </wsdl:input>
      <wsdl:output message="tns:DownloadCodesResponse" name="DownloadCodesResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetProduct">
      <wsdl:input message="tns:GetProductRequest" name="GetProductRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetProductResponse" name="GetProductResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListCodePatterns">
      <wsdl:input message="tns:ListCodePatternsRequest" name="ListCodePatternsRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListCodePatternsResponse" name="ListCodePatternsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateNewSectionInRoll">
      <wsdl:input message="tns:CreateNewSectionInRollRequest" name="CreateNewSectionInRollRequest">
    </wsdl:input>
      <wsdl:output message="tns:CreateNewSectionInRollResponse" name="CreateNewSectionInRollResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodesProducedByProduct">
      <wsdl:input message="tns:GetCodesProducedByProductRequest" name="GetCodesProducedByProductRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetCodesProducedByProductResponse" name="GetCodesProducedByProductResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ValidationsLogFilter">
      <wsdl:input message="tns:ValidationsLogFilterRequest" name="ValidationsLogFilterRequest">
    </wsdl:input>
      <wsdl:output message="tns:ValidationsLogFilterResponse" name="ValidationsLogFilterResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateOrderSectionMetadata">
      <wsdl:input message="tns:UpdateOrderSectionMetadataRequest" name="UpdateOrderSectionMetadataRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateOrderSectionMetadataResponse" name="UpdateOrderSectionMetadataResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteEntryChannel">
      <wsdl:input message="tns:DeleteEntryChannelRequest" name="DeleteEntryChannelRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteEntryChannelResponse" name="DeleteEntryChannelResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateOrderMetadata">
      <wsdl:input message="tns:UpdateOrderMetadataRequest" name="UpdateOrderMetadataRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateOrderMetadataResponse" name="UpdateOrderMetadataResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodesProducedByUser">
      <wsdl:input message="tns:GetCodesProducedByUserRequest" name="GetCodesProducedByUserRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetCodesProducedByUserResponse" name="GetCodesProducedByUserResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodeStatusChanges">
      <wsdl:input message="tns:GetCodeStatusChangesRequest" name="GetCodeStatusChangesRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetCodeStatusChangesResponse" name="GetCodeStatusChangesResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateAti">
      <wsdl:input message="tns:UpdateAtiRequest" name="UpdateAtiRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateAtiResponse" name="UpdateAtiResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeValidator">
      <wsdl:input message="tns:CodeValidatorRequest" name="CodeValidatorRequest">
    </wsdl:input>
      <wsdl:output message="tns:CodeValidatorResponse" name="CodeValidatorResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeDissector">
      <wsdl:input message="tns:CodeDissectorRequest" name="CodeDissectorRequest">
    </wsdl:input>
      <wsdl:output message="tns:CodeDissectorResponse" name="CodeDissectorResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AppCodeValidator">
      <wsdl:input message="tns:AppCodeValidatorRequest" name="AppCodeValidatorRequest">
    </wsdl:input>
      <wsdl:output message="tns:AppCodeValidatorResponse" name="AppCodeValidatorResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CustomerCodeDissector">
      <wsdl:input message="tns:CustomerCodeDissectorRequest" name="CustomerCodeDissectorRequest">
    </wsdl:input>
      <wsdl:output message="tns:CustomerCodeDissectorResponse" name="CustomerCodeDissectorResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetRoll">
      <wsdl:input message="tns:GetRollRequest" name="GetRollRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetRollResponse" name="GetRollResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="SetCodeStatusForOrder">
      <wsdl:input message="tns:SetCodeStatusForOrderRequest" name="SetCodeStatusForOrderRequest">
    </wsdl:input>
      <wsdl:output message="tns:SetCodeStatusForOrderResponse" name="SetCodeStatusForOrderResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ApplyAtiGroup">
      <wsdl:input message="tns:ApplyAtiGroupRequest" name="ApplyAtiGroupRequest">
    </wsdl:input>
      <wsdl:output message="tns:ApplyAtiGroupResponse" name="ApplyAtiGroupResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="LockOrder">
      <wsdl:input message="tns:LockOrderRequest" name="LockOrderRequest">
    </wsdl:input>
      <wsdl:output message="tns:LockOrderResponse" name="LockOrderResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateEntryChannel">
      <wsdl:input message="tns:UpdateEntryChannelRequest" name="UpdateEntryChannelRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateEntryChannelResponse" name="UpdateEntryChannelResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="Statistics">
      <wsdl:input message="tns:StatisticsRequest" name="StatisticsRequest">
    </wsdl:input>
      <wsdl:output message="tns:StatisticsResponse" name="StatisticsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="IPLocalization">
      <wsdl:input message="tns:IPLocalizationRequest" name="IPLocalizationRequest">
    </wsdl:input>
      <wsdl:output message="tns:IPLocalizationResponse" name="IPLocalizationResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ExpansionsStatus">
      <wsdl:input message="tns:ExpansionsStatusRequest" name="ExpansionsStatusRequest">
    </wsdl:input>
      <wsdl:output message="tns:ExpansionsStatusResponse" name="ExpansionsStatusResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeBlacklistRemove">
      <wsdl:input message="tns:CodeBlacklistRemoveRequest" name="CodeBlacklistRemoveRequest">
    </wsdl:input>
      <wsdl:output message="tns:CodeBlacklistRemoveResponse" name="CodeBlacklistRemoveResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteMetadataSchema">
      <wsdl:input message="tns:DeleteMetadataSchemaRequest" name="DeleteMetadataSchemaRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteMetadataSchemaResponse" name="DeleteMetadataSchemaResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteOrderSectionMetadata">
      <wsdl:input message="tns:DeleteOrderSectionMetadataRequest" name="DeleteOrderSectionMetadataRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteOrderSectionMetadataResponse" name="DeleteOrderSectionMetadataResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ExpansionsInfo">
      <wsdl:input message="tns:ExpansionsInfoRequest" name="ExpansionsInfoRequest">
    </wsdl:input>
      <wsdl:output message="tns:ExpansionsInfoResponse" name="ExpansionsInfoResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListExpansions">
      <wsdl:input message="tns:ListExpansionsRequest" name="ListExpansionsRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListExpansionsResponse" name="ListExpansionsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadRoll">
      <wsdl:input message="tns:ReadRollRequest" name="ReadRollRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadRollResponse" name="ReadRollResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodeStatusHistory">
      <wsdl:input message="tns:GetCodeStatusHistoryRequest" name="GetCodeStatusHistoryRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetCodeStatusHistoryResponse" name="GetCodeStatusHistoryResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateSection">
      <wsdl:input message="tns:UpdateSectionRequest" name="UpdateSectionRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateSectionResponse" name="UpdateSectionResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateOrderData">
      <wsdl:input message="tns:UpdateOrderDataRequest" name="UpdateOrderDataRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateOrderDataResponse" name="UpdateOrderDataResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="RenameAti">
      <wsdl:input message="tns:RenameAtiRequest" name="RenameAtiRequest">
    </wsdl:input>
      <wsdl:output message="tns:RenameAtiResponse" name="RenameAtiResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateCodeConfig">
      <wsdl:input message="tns:CreateCodeConfigRequest" name="CreateCodeConfigRequest">
    </wsdl:input>
      <wsdl:output message="tns:CreateCodeConfigResponse" name="CreateCodeConfigResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListEntryChannels">
      <wsdl:input message="tns:ListEntryChannelsRequest" name="ListEntryChannelsRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListEntryChannelsResponse" name="ListEntryChannelsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ApplyAti">
      <wsdl:input message="tns:ApplyAtiRequest" name="ApplyAtiRequest">
    </wsdl:input>
      <wsdl:output message="tns:ApplyAtiResponse" name="ApplyAtiResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadOrder">
      <wsdl:input message="tns:ReadOrderRequest" name="ReadOrderRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadOrderResponse" name="ReadOrderResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetExpansion">
      <wsdl:input message="tns:GetExpansionRequest" name="GetExpansionRequest">
    </wsdl:input>
      <wsdl:output message="tns:GetExpansionResponse" name="GetExpansionResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateOrder">
      <wsdl:input message="tns:UpdateOrderRequest" name="UpdateOrderRequest">
    </wsdl:input>
      <wsdl:output message="tns:UpdateOrderResponse" name="UpdateOrderResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteAti">
      <wsdl:input message="tns:DeleteAtiRequest" name="DeleteAtiRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteAtiResponse" name="DeleteAtiResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="MapExpansionsToSections">
      <wsdl:input message="tns:MapExpansionsToSectionsRequest" name="MapExpansionsToSectionsRequest">
    </wsdl:input>
      <wsdl:output message="tns:MapExpansionsToSectionsResponse" name="MapExpansionsToSectionsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadAtiGroup">
      <wsdl:input message="tns:ReadAtiGroupRequest" name="ReadAtiGroupRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadAtiGroupResponse" name="ReadAtiGroupResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="BatchCodeValidator">
      <wsdl:input message="tns:BatchCodeValidatorRequest" name="BatchCodeValidatorRequest">
    </wsdl:input>
      <wsdl:output message="tns:BatchCodeValidatorResponse" name="BatchCodeValidatorResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="InitOrder">
      <wsdl:input message="tns:InitOrderRequest" name="InitOrderRequest">
    </wsdl:input>
      <wsdl:output message="tns:InitOrderResponse" name="InitOrderResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateSsccSequence">
      <wsdl:input message="tns:CreateSsccSequenceRequest" name="CreateSsccSequenceRequest">
    </wsdl:input>
      <wsdl:output message="tns:CreateSsccSequenceResponse" name="CreateSsccSequenceResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteSection">
      <wsdl:input message="tns:DeleteSectionRequest" name="DeleteSectionRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteSectionResponse" name="DeleteSectionResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadSsccSequence">
      <wsdl:input message="tns:ReadSsccSequenceRequest" name="ReadSsccSequenceRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadSsccSequenceResponse" name="ReadSsccSequenceResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="IdentifyRoll">
      <wsdl:input message="tns:IdentifyRollRequest" name="IdentifyRollRequest">
    </wsdl:input>
      <wsdl:output message="tns:IdentifyRollResponse" name="IdentifyRollResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteAtiGroup">
      <wsdl:input message="tns:DeleteAtiGroupRequest" name="DeleteAtiGroupRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteAtiGroupResponse" name="DeleteAtiGroupResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListMetadataSchemas">
      <wsdl:input message="tns:ListMetadataSchemasRequest" name="ListMetadataSchemasRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListMetadataSchemasResponse" name="ListMetadataSchemasResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListReservedSsccSequence">
      <wsdl:input message="tns:ListReservedSsccSequenceRequest" name="ListReservedSsccSequenceRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListReservedSsccSequenceResponse" name="ListReservedSsccSequenceResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadOrderSectionMetadata">
      <wsdl:input message="tns:ReadOrderSectionMetadataRequest" name="ReadOrderSectionMetadataRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadOrderSectionMetadataResponse" name="ReadOrderSectionMetadataResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListProductMetadataSchemas">
      <wsdl:input message="tns:ListProductMetadataSchemasRequest" name="ListProductMetadataSchemasRequest">
    </wsdl:input>
      <wsdl:output message="tns:ListProductMetadataSchemasResponse" name="ListProductMetadataSchemasResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="BatchValidationDetails">
      <wsdl:input message="tns:BatchValidationDetailsRequest" name="BatchValidationDetailsRequest">
    </wsdl:input>
      <wsdl:output message="tns:BatchValidationDetailsResponse" name="BatchValidationDetailsResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="MarkTemporaryRollEnd">
      <wsdl:input message="tns:MarkTemporaryRollEndRequest" name="MarkTemporaryRollEndRequest">
    </wsdl:input>
      <wsdl:output message="tns:MarkTemporaryRollEndResponse" name="MarkTemporaryRollEndResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteOrderMetadata">
      <wsdl:input message="tns:DeleteOrderMetadataRequest" name="DeleteOrderMetadataRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteOrderMetadataResponse" name="DeleteOrderMetadataResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteProduct">
      <wsdl:input message="tns:DeleteProductRequest" name="DeleteProductRequest">
    </wsdl:input>
      <wsdl:output message="tns:DeleteProductResponse" name="DeleteProductResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadOrderMetadata">
      <wsdl:input message="tns:ReadOrderMetadataRequest" name="ReadOrderMetadataRequest">
    </wsdl:input>
      <wsdl:output message="tns:ReadOrderMetadataResponse" name="ReadOrderMetadataResponse">
    </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ActivateSection">
      <wsdl:input message="tns:ActivateSectionRequest" name="ActivateSectionRequest">
    </wsdl:input>
      <wsdl:output message="tns:ActivateSectionResponse" name="ActivateSectionResponse">
    </wsdl:output>
    </wsdl:operation>
  </wsdl:portType>
  <wsdl:binding name="kcengineSoap11" type="tns:kcengine">
    <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
    <wsdl:operation name="ApplyAtiTemplateGroup">
      <soap:operation soapAction=""/>
      <wsdl:input name="ApplyAtiTemplateGroupRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ApplyAtiTemplateGroupResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateEntryChannel">
      <soap:operation soapAction=""/>
      <wsdl:input name="CreateEntryChannelRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CreateEntryChannelResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadCodeConfig">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadCodeConfigRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadCodeConfigResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListSections">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListSectionsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListSectionsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetOrderSectionsValidations">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetOrderSectionsValidationsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetOrderSectionsValidationsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ActivateRollSection">
      <soap:operation soapAction=""/>
      <wsdl:input name="ActivateRollSectionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ActivateRollSectionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateProduct">
      <soap:operation soapAction=""/>
      <wsdl:input name="CreateProductRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CreateProductResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCode">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetCodeRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetCodeResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadSscc">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadSsccRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadSsccResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="MultiExpandOrder">
      <soap:operation soapAction=""/>
      <wsdl:input name="MultiExpandOrderRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="MultiExpandOrderResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadAti">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadAtiRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadAtiResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeBlacklistAdd">
      <soap:operation soapAction=""/>
      <wsdl:input name="CodeBlacklistAddRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CodeBlacklistAddResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadCodeStatusConfig">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadCodeStatusConfigRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadCodeStatusConfigResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListExpansionCodes">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListExpansionCodesRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListExpansionCodesResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListAtis">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListAtisRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListAtisResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListAtiGroups">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListAtiGroupsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListAtiGroupsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateAtiGroup">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateAtiGroupRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateAtiGroupResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ExpandOrder">
      <soap:operation soapAction=""/>
      <wsdl:input name="ExpandOrderRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ExpandOrderResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodesProducedByGroup">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetCodesProducedByGroupRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetCodesProducedByGroupResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="BatchValidationsLog">
      <soap:operation soapAction=""/>
      <wsdl:input name="BatchValidationsLogRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="BatchValidationsLogResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AddAtiGroup">
      <soap:operation soapAction=""/>
      <wsdl:input name="AddAtiGroupRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="AddAtiGroupResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="SetCodeStatus">
      <soap:operation soapAction=""/>
      <wsdl:input name="SetCodeStatusRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="SetCodeStatusResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DiskUsage">
      <soap:operation soapAction=""/>
      <wsdl:input name="DiskUsageRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DiskUsageResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeBlacklist">
      <soap:operation soapAction=""/>
      <wsdl:input name="CodeBlacklistRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CodeBlacklistResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListOrders">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListOrdersRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListOrdersResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListAllExpansions">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListAllExpansionsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListAllExpansionsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateCodeStatusConfig">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateCodeStatusConfigRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateCodeStatusConfigResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateEntryChannelTranslations">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateEntryChannelTranslationsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateEntryChannelTranslationsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="WorkersInfo">
      <soap:operation soapAction=""/>
      <wsdl:input name="WorkersInfoRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="WorkersInfoResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="StatisticsLastOrderedExpansions">
      <soap:operation soapAction=""/>
      <wsdl:input name="StatisticsLastOrderedExpansionsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="StatisticsLastOrderedExpansionsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodeStatusConfig">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetCodeStatusConfigRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetCodeStatusConfigResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteProductMetadataSchema">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteProductMetadataSchemaRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteProductMetadataSchemaResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="SetDefaultMetadataSchema">
      <soap:operation soapAction=""/>
      <wsdl:input name="SetDefaultMetadataSchemaRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="SetDefaultMetadataSchemaResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteLastExpansion">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteLastExpansionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteLastExpansionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CalibrateRoll">
      <soap:operation soapAction=""/>
      <wsdl:input name="CalibrateRollRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CalibrateRollResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetOrderValidations">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetOrderValidationsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetOrderValidationsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadSection">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadSectionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadSectionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetEntryChannel">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetEntryChannelRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetEntryChannelResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DefaultAtiGroup">
      <soap:operation soapAction=""/>
      <wsdl:input name="DefaultAtiGroupRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DefaultAtiGroupResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateSection">
      <soap:operation soapAction=""/>
      <wsdl:input name="CreateSectionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CreateSectionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AddAti">
      <soap:operation soapAction=""/>
      <wsdl:input name="AddAtiRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="AddAtiResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteReservedSsccSequence">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteReservedSsccSequenceRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteReservedSsccSequenceResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AddReservedSsccSequence">
      <soap:operation soapAction=""/>
      <wsdl:input name="AddReservedSsccSequenceRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="AddReservedSsccSequenceResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListProducts">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListProductsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListProductsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AddCodeStatusConfig">
      <soap:operation soapAction=""/>
      <wsdl:input name="AddCodeStatusConfigRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="AddCodeStatusConfigResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="StatisticsLastOrders">
      <soap:operation soapAction=""/>
      <wsdl:input name="StatisticsLastOrdersRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="StatisticsLastOrdersResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="FindLookAlikeCode">
      <soap:operation soapAction=""/>
      <wsdl:input name="FindLookAlikeCodeRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="FindLookAlikeCodeResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="SetExpansionStatus">
      <soap:operation soapAction=""/>
      <wsdl:input name="SetExpansionStatusRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="SetExpansionStatusResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateProduct">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateProductRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateProductResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetOrderExpansionsValidations">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetOrderExpansionsValidationsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetOrderExpansionsValidationsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListSectionAtis">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListSectionAtisRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListSectionAtisResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="StatisticsLastProducedExpansions">
      <soap:operation soapAction=""/>
      <wsdl:input name="StatisticsLastProducedExpansionsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="StatisticsLastProducedExpansionsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UnlinkAti">
      <soap:operation soapAction=""/>
      <wsdl:input name="UnlinkAtiRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UnlinkAtiResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListCodeConfigs">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListCodeConfigsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListCodeConfigsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeactivateSection">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeactivateSectionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeactivateSectionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UnlinkAllAtis">
      <soap:operation soapAction=""/>
      <wsdl:input name="UnlinkAllAtisRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UnlinkAllAtisResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeActivateSectionInRoll">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeActivateSectionInRollRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeActivateSectionInRollResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetOrderCodeStatusStatistics">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetOrderCodeStatusStatisticsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetOrderCodeStatusStatisticsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DownloadCodes">
      <soap:operation soapAction=""/>
      <wsdl:input name="DownloadCodesRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DownloadCodesResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetProduct">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetProductRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetProductResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListCodePatterns">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListCodePatternsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListCodePatternsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateNewSectionInRoll">
      <soap:operation soapAction=""/>
      <wsdl:input name="CreateNewSectionInRollRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CreateNewSectionInRollResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodesProducedByProduct">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetCodesProducedByProductRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetCodesProducedByProductResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ValidationsLogFilter">
      <soap:operation soapAction=""/>
      <wsdl:input name="ValidationsLogFilterRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ValidationsLogFilterResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateOrderSectionMetadata">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateOrderSectionMetadataRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateOrderSectionMetadataResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteEntryChannel">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteEntryChannelRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteEntryChannelResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateOrderMetadata">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateOrderMetadataRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateOrderMetadataResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodesProducedByUser">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetCodesProducedByUserRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetCodesProducedByUserResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodeStatusChanges">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetCodeStatusChangesRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetCodeStatusChangesResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateAti">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateAtiRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateAtiResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeValidator">
      <soap:operation soapAction=""/>
      <wsdl:input name="CodeValidatorRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CodeValidatorResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeDissector">
      <soap:operation soapAction=""/>
      <wsdl:input name="CodeDissectorRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CodeDissectorResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="AppCodeValidator">
      <soap:operation soapAction=""/>
      <wsdl:input name="AppCodeValidatorRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="AppCodeValidatorResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CustomerCodeDissector">
      <soap:operation soapAction=""/>
      <wsdl:input name="CustomerCodeDissectorRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CustomerCodeDissectorResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetRoll">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetRollRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetRollResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="SetCodeStatusForOrder">
      <soap:operation soapAction=""/>
      <wsdl:input name="SetCodeStatusForOrderRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="SetCodeStatusForOrderResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ApplyAtiGroup">
      <soap:operation soapAction=""/>
      <wsdl:input name="ApplyAtiGroupRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ApplyAtiGroupResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="LockOrder">
      <soap:operation soapAction=""/>
      <wsdl:input name="LockOrderRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="LockOrderResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateEntryChannel">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateEntryChannelRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateEntryChannelResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="Statistics">
      <soap:operation soapAction=""/>
      <wsdl:input name="StatisticsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="StatisticsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="IPLocalization">
      <soap:operation soapAction=""/>
      <wsdl:input name="IPLocalizationRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="IPLocalizationResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ExpansionsStatus">
      <soap:operation soapAction=""/>
      <wsdl:input name="ExpansionsStatusRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ExpansionsStatusResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CodeBlacklistRemove">
      <soap:operation soapAction=""/>
      <wsdl:input name="CodeBlacklistRemoveRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CodeBlacklistRemoveResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteMetadataSchema">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteMetadataSchemaRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteMetadataSchemaResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteOrderSectionMetadata">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteOrderSectionMetadataRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteOrderSectionMetadataResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ExpansionsInfo">
      <soap:operation soapAction=""/>
      <wsdl:input name="ExpansionsInfoRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ExpansionsInfoResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListExpansions">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListExpansionsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListExpansionsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadRoll">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadRollRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadRollResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetCodeStatusHistory">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetCodeStatusHistoryRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetCodeStatusHistoryResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateSection">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateSectionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateSectionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateOrderData">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateOrderDataRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateOrderDataResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="RenameAti">
      <soap:operation soapAction=""/>
      <wsdl:input name="RenameAtiRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="RenameAtiResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateCodeConfig">
      <soap:operation soapAction=""/>
      <wsdl:input name="CreateCodeConfigRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CreateCodeConfigResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListEntryChannels">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListEntryChannelsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListEntryChannelsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ApplyAti">
      <soap:operation soapAction=""/>
      <wsdl:input name="ApplyAtiRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ApplyAtiResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadOrder">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadOrderRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadOrderResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="GetExpansion">
      <soap:operation soapAction=""/>
      <wsdl:input name="GetExpansionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="GetExpansionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="UpdateOrder">
      <soap:operation soapAction=""/>
      <wsdl:input name="UpdateOrderRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="UpdateOrderResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteAti">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteAtiRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteAtiResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="MapExpansionsToSections">
      <soap:operation soapAction=""/>
      <wsdl:input name="MapExpansionsToSectionsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="MapExpansionsToSectionsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadAtiGroup">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadAtiGroupRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadAtiGroupResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="BatchCodeValidator">
      <soap:operation soapAction=""/>
      <wsdl:input name="BatchCodeValidatorRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="BatchCodeValidatorResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="InitOrder">
      <soap:operation soapAction=""/>
      <wsdl:input name="InitOrderRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="InitOrderResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="CreateSsccSequence">
      <soap:operation soapAction=""/>
      <wsdl:input name="CreateSsccSequenceRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="CreateSsccSequenceResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteSection">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteSectionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteSectionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadSsccSequence">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadSsccSequenceRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadSsccSequenceResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="IdentifyRoll">
      <soap:operation soapAction=""/>
      <wsdl:input name="IdentifyRollRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="IdentifyRollResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteAtiGroup">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteAtiGroupRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteAtiGroupResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListMetadataSchemas">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListMetadataSchemasRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListMetadataSchemasResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListReservedSsccSequence">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListReservedSsccSequenceRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListReservedSsccSequenceResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadOrderSectionMetadata">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadOrderSectionMetadataRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadOrderSectionMetadataResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ListProductMetadataSchemas">
      <soap:operation soapAction=""/>
      <wsdl:input name="ListProductMetadataSchemasRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ListProductMetadataSchemasResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="BatchValidationDetails">
      <soap:operation soapAction=""/>
      <wsdl:input name="BatchValidationDetailsRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="BatchValidationDetailsResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="MarkTemporaryRollEnd">
      <soap:operation soapAction=""/>
      <wsdl:input name="MarkTemporaryRollEndRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="MarkTemporaryRollEndResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteOrderMetadata">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteOrderMetadataRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteOrderMetadataResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="DeleteProduct">
      <soap:operation soapAction=""/>
      <wsdl:input name="DeleteProductRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="DeleteProductResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ReadOrderMetadata">
      <soap:operation soapAction=""/>
      <wsdl:input name="ReadOrderMetadataRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ReadOrderMetadataResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="ActivateSection">
      <soap:operation soapAction=""/>
      <wsdl:input name="ActivateSectionRequest">
        <soap:body use="literal"/>
      </wsdl:input>
      <wsdl:output name="ActivateSectionResponse">
        <soap:body use="literal"/>
      </wsdl:output>
    </wsdl:operation>
  </wsdl:binding>
  <wsdl:service name="kcengineService">
    <wsdl:port binding="tns:kcengineSoap11" name="kcengineSoap11">
      <soap:address location="192.168.0.193/ssp/kcengine-ws"/>
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>'''
