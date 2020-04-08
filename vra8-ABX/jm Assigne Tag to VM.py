/** Assigns tags to a machine
 * @param {Object} inputs
 * @param {Object} inputs.tags - The initial tags for the machine, supplied from the event data
 *                 during actual provisioning or from user input for testing purposes.
 * @param {Object} inputs.newTags - The tags to assign to the machine, which can be
 *                 in the form {"name": "value"} for name=value tags
 *                 or {"name": ""} for a simple name tag.
 * @returns {Object} The desired tags.
 */
 
def handler(context, inputs):
    new_tags = inputs.new_tags;
    outputs = {};
    outputs.tags = inputs.tags;

    for key, value in new_tags.item() {
        outputs.tags[key] = value;
    };

/*    console.log("Setting tags: " + JSON.stringify(newTags));
    print("jm Setting tags: {0}".format(new_tags))
    
    return outputs;

