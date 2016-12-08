import sys


template = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:com="http://www.alcatellucent.com/dsc/provisioningapi/common" xmlns:sub="http://www.alcatellucent.com/dsc/provisioningapi/70/subscriber">
   <soapenv:Header>
      <com:header>
         <com:clientAppId>whatever</com:clientAppId>
         <com:requestId>request1</com:requestId>
      </com:header>
   </soapenv:Header>
   <soapenv:Body>
      <sub:addAccount>
         <!--Optional:-->
         <sub:account>
            <sub:accountId>?ACCT#?</sub:accountId>
            <!--Optional:-->
            <sub:owningRealm>ims-wcw4glte.com</sub:owningRealm>
            <!--Optional:-->
            <sub:resetDayOfMonth>1</sub:resetDayOfMonth>
            <!--Optional:-->
            <sub:resetDayOfWeek>SUNDAY</sub:resetDayOfWeek>
            <!--Optional:-->
            <sub:resetHourOfDay>7</sub:resetHourOfDay>
            <!--Optional:-->
            <sub:unknownAccount>false</sub:unknownAccount>
            <!--Optional:-->
            <sub:subscribers>
               <!--Zero or more repetitions:-->
               <sub:subscriber>
                  <!--Optional:-->
                  <sub:accountId>?ACCT#?</sub:accountId>
                  <sub:userId>?IMSI?</sub:userId>
                  <!--Optional:-->
                  <sub:state>ENABLED</sub:state>
                  <!--Optional:-->
                  <sub:subscriptionIds>
                     <!--Zero or more repetitions:-->
                     <sub:subscriptionId>
                        <sub:value>?IMSI?</sub:value>
                        <sub:type>END_USER_IMSI</sub:type>
                     </sub:subscriptionId>
                     <sub:subscriptionId>
                        <sub:value>?MSISDN?</sub:value>
                        <sub:type>END_USER_E164</sub:type>
                     </sub:subscriptionId>
                  </sub:subscriptionIds>
                  <!--Optional:-->
                  <sub:notificationConfig>
                     <sub:notifyableByEmail>false</sub:notifyableByEmail>
                     <sub:notifyableBySMS>false</sub:notifyableBySMS>
                  </sub:notificationConfig>
                  <!--Optional:-->
                  <sub:allowOverage>true</sub:allowOverage>
                  <!--Optional:-->
                  <sub:syOCSEnabled>false</sub:syOCSEnabled>
               </sub:subscriber>
            </sub:subscribers>
            <!--Optional:-->
            <sub:meteredServices>
               <!--Zero or more repetitions:-->
               <sub:meteredService>
                  <sub:name>?Rule_name?</sub:name>
                  <sub:serviceType>METERING_LIMIT</sub:serviceType>
                  <!--Optional:-->
                  <sub:defaultQuotaPrivilege>
                     <sub:hasAccess>true</sub:hasAccess>
                     <sub:quotaShareType>VALUE</sub:quotaShareType>
                     <sub:quotaShareCap>-1</sub:quotaShareCap>
                  </sub:defaultQuotaPrivilege>
                  <!--Zero or more repetitions:-->
                  <sub:quotaShares>
                     <sub:userId>?IMSI?</sub:userId>
                     <sub:quotaPrivilege>
                        <sub:hasAccess>true</sub:hasAccess>
                        <sub:quotaShareType>VALUE</sub:quotaShareType>
                        <sub:quotaShareCap>-1</sub:quotaShareCap>
                     </sub:quotaPrivilege>
                  </sub:quotaShares>
               </sub:meteredService>
            </sub:meteredServices>
         </sub:account>
      </sub:addAccount>
   </soapenv:Body>
</soapenv:Envelope>'''
input_data = open('PCRF_Fixed_sampledata.csv')
'''
Data format in input file to be:
IMSI,MSISDN,Acct #,Name(optional),Applied Rule
Each entry in its own row
'''
for row in input_data:
    inlist = row.split(',')
    test = template.replace("?ACCT#?", inlist[2])
    test = test.replace("?IMSI?", inlist[0])
    test = test.replace("?MSISDN?", inlist[1])
    test = test.replace("?Rule_name?", inlist[4])
    print(test)