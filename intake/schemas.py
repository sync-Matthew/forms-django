CREATE_FORM_SCHEMA = {
    "title": "Customer Feedback",
    "description": "Form to collect customer feedback",
}


READ_FORM_SCHEMA = {
    "user_id": "a0b81346-aaf9-4745-8b58-335af845b879",
    "title": "Customer Feedback",
    "description": "Form to collect customer feedback",
    "created_at": "2024-08-25T03:30:26.898782Z",
    "updated_at": "2024-08-25T03:30:26.898851Z",
}

CREATE_SECTION_SCHEMA = {
    "form_id": 3,
    "title": "Personal Information",
    "position": 1,
}

READ_SECTION_SCHEMA = {
    "id": 5,
    "form_id": 3,
    "title": "Personal Information",
    "position": 1,
    "created_at": "2024-08-25T03:30:26.898782Z",
    "updated_at": "2024-08-25T03:30:26.898851Z",
}

CREATE_ROW_SCHEMA = {
    "section_id": 5,
    "position": 1,
}

READ_ROW_SCHEMA = {
    "id": 7,
    "section_id": 5,
    "position": 1,
    "created_at": "2024-08-25T03:30:26.898782Z",
    "updated_at": "2024-08-25T03:30:26.898851Z",
}

CREATE_FIELD_SCHEMA = {
    "quickbase_id": 123456,
    "row_id": 7,
    "position": 1,
}

READ_FIELD_SCHEMA = {
    "id": 9,
    "quickbase_id": 123456,
    "row_id": 7,
    "position": 1,
    "created_at": "2024-08-25T03:30:26.898782Z",
    "updated_at": "2024-08-25T03:30:26.898851Z",
}