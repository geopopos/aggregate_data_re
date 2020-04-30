from aggregate_data import aggregate_data


def test_example_data():
    rad_input = [
        {"rad_exam_id": 1, "modality": "CT", "exam_duration": 10},
        {"rad_exam_id": 2, "modality": "CT", "exam_duration": 13},
        {"rad_exam_id": 3, "modality": "CT", "exam_duration": 12},
        {"rad_exam_id": 4, "modality": "MR", "exam_duration": 90},
        {"rad_exam_id": 5, "modality": "MR", "exam_duration": 100},
        {"rad_exam_id": 6, "modality": "US", "exam_duration": 9},
        {"rad_exam_id": 7, "modality": "US", "exam_duration": 7},
    ]
    output = [
        {"label": "CT", "value": 35},
        {"label": "MR", "value": 190},
        {"label": "US", "value": 16},
    ]

    assert aggregate_data(rad_input) == output
