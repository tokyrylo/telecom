### Rooms

| Field | Type | Description |
| ----- | ---- | ----------- |
| id    | int  | Unique ID   |
| name  | str  | Name (example, "Alpha") |
| capacity | int | Room capacity (2-20)  |


### Booking

| Field   | Type | Description |
| ------- | ---- | ----------- | 
|  id     | int  | Unique ID   |
| room_id | int  | Room ID     |
| user_id | int  | User ID     |
| start_time | datetime   | Start of booking   |
| end_time   | datetime   | End of room reservation |
