mport boto3

regionsarea = ["us-east-1", "us-east-2", "us-west-1", "us-west-2", "ap-south-1", "us-west-1", "us-west-2", "ap-south-1",
               "ap-northeast-3", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "ca-central-1",
               "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-north-1", "sa-east-1"]


# ,,,,,,"cn-north-1",,"cn-northwest-1"]
def tagging(resourcename, resourceid, region, missingkeys):
    jsonvalue = {}
    jsonvalue['resourcename'] = resourcename
    resourceidtype = resourceid.split("/")
    jsonvalue['resourceidtype'] = resourceidtype[0]
    jsonvalue['resource'] = resourceidtype[1:]
    jsonvalue['region'] = region
    jsonvalue['missingKeys'] = missingkeys

    return jsonvalue


def tag():
    filemain = ""
    for area in regionsarea:
        client = boto3.client('resourcegroupstaggingapi', region_name=area)
        s3 = boto3.client('s3', region_name=area)
        response = client.get_resources()
        resources = response['ResourceTagMappingList']
        taggingKeys = ['Name', 'CostCentre', "owner", "Environment"]
        for resourcetag in resources:
            keyshaving = taggingKeys
            if (resourcetag['Tags']):
                for tag in resourcetag['Tags']:
                    if tag["Key"] in keyshaving:
                        keyshaving.remove(tag["Key"])
                resourcearn = resourcetag['ResourceARN'].split(":")
                filemain = filemain + str(tagging(resourcearn[2], resourcearn[5], resourcearn[3], keyshaving)) + "\n"
            else:
                getting = resourcetag['ResourceARN'].split(":")
                tagging(getting[2], getting[5], getting[3], keyshaving)
                filemain = filemain + str(tagging(resourcearn[2], resourcearn[5], resourcearn[3], keyshaving)) + "\n"

    s3response = s3.put_object(
        Body=filemain,
        Bucket='<BUCKET-Name>',
        Key='notagresources.txt'
    )
    print(filemain)
    return

tag()