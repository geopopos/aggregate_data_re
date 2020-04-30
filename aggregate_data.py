def aggregate_data(rad_input):
    output = []
    
    labels = []
    # loop over the input array
    for data in rad_input:
        # for datapoint check if modality is already in the sum object
        if data["modality"] in labels:
            # add the "exam_duration" to the "value"
            for out in output:
                if out["label"] == data["modality"]:
                    out["value"] += data["exam_duration"]
        else:
            labels.append(data["modality"])
            # add a new sum_object to the output array
            # add the datapoints "exam_duration" to the "value" of the new sum
            # object
            sum_object = {
                "label": data["modality"],
                "value": data["exam_duration"]
            }
            output.append(sum_object)
    return output
