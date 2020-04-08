def handler(context, inputs):
    
    old_name = inputs["resourceNames"][0]
    new_name = inputs["customProperties"]["jm-newName"]
    
    outputs = {}
    outputs["resourceNames"] = inputs["resourceNames"]
    outputs["resourceNames"][0] = new_name
    
    print("Changing Name from {0} --to-- {1}".format(old_name, new_name))

    return outputs
