
var DB = db.getSiblingDB('free5gc');
var i=0;
var j=208930000000001;
var plmn="20893";
var UE_COUNT=1000;

while(i < UE_COUNT){
        var imsi="imsi-"+(i+j).toString();
        db.policyData.ues.amData.insertOne(
          {
                subscCats: [ 'free5gc' ],
                ueId: imsi
          });
        db.policyData.ues.smData.insertOne(
          {
                smPolicySnssaiData: {
                  '01010203': {
                        snssai: { sst: 1, sd: '010203' },
                        smPolicyDnnData: {
                          internet2: { dnn: 'internet2' },
                          internet: { dnn: 'internet' }
                        }
                  }
                },
                ueId: imsi
          });
        db.subscriptionData.authenticationData.authenticationSubscription.insertOne(
          {
                authenticationMethod: '5G_AKA',
                permanentKey: {
                  encryptionAlgorithm: 0,
                  encryptionKey: 0,
                  permanentKeyValue: '8baf473f2f8fd09487cccbd7097c6862'
                },
                sequenceNumber: '16f3b3f710d5',
                authenticationManagementField: '8000',
                milenage: { op: { encryptionAlgorithm: 0, encryptionKey: 0, opValue: '' } },
                opc: {
                  encryptionAlgorithm: 0,
                  encryptionKey: 0,
                  opcValue: '8e27b6af0e692e750f32667a3b14605d'
                },
                ueId: imsi
          });
        db.subscriptionData.provisionedData.amData.insertOne(
          {
                ueId: imsi,
                servingPlmnId: plmn,
                gpsis: [ 'msisdn-0900000000' ],
                subscribedUeAmbr: { uplink: '1 Gbps', downlink: '2 Gbps' },
                nssai: {
                  defaultSingleNssais: [ { sst: 1, sd: '010203' }, { sst: 1, sd: '010203' } ]
                }
          });
        db.subscriptionData.provisionedData.smData.insertOne(
          {
                servingPlmnId: plmn,
                singleNssai: { sst: 1, sd: '010203' },
                dnnConfigurations: {
                  internet: {
                        pduSessionTypes: { defaultSessionType: 'IPV4', allowedSessionTypes: [ 'IPV4' ] },
                        sscModes: {
                          allowedSscModes: [ 'SSC_MODE_2', 'SSC_MODE_3' ],
                          defaultSscMode: 'SSC_MODE_1'
                        },
                        '5gQosProfile': {
                          arp: { priorityLevel: 8, preemptCap: '', preemptVuln: '' },
                          priorityLevel: 8,
                          '5qi': 9
                        },
                        sessionAmbr: { uplink: '200 Mbps', downlink: '100 Mbps' }
                  },
                  internet2: {
                        sessionAmbr: { downlink: '100 Mbps', uplink: '200 Mbps' },
                        pduSessionTypes: { defaultSessionType: 'IPV4', allowedSessionTypes: [ 'IPV4' ] },
                        sscModes: {
                          defaultSscMode: 'SSC_MODE_1',
                          allowedSscModes: [ 'SSC_MODE_2', 'SSC_MODE_3' ]
                        },
                        '5gQosProfile': {
                          '5qi': 9,
                          arp: { priorityLevel: 8, preemptCap: '', preemptVuln: '' },
                          priorityLevel: 8
                        }
                  }
                },
                ueId: imsi
          });
        db.subscriptionData.provisionedData.smfSelectionSubscriptionData.insertOne(
          {
                servingPlmnId: plmn,
                subscribedSnssaiInfos: {
                  '01010203': { dnnInfos: [ { dnn: 'internet' }, { dnn: 'internet2' } ] }
                },
                ueId: imsi
          });
        i++;
}
//docker cp insert_db.js mongodb:/opt
//docker exec -it mongodb mongosh mongodb://127.0.0.1:27017/free5gc insert_db.js
// get count:
// db.policyData.ues.smData.aggregate([{ $group: { _id: null, count: { $sum: 1 } } }])