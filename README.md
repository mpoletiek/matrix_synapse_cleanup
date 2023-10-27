# matrix_synapse_cleanup
Cleanup scripts for Matrix server Synapse.

## Setup
Modify `.env.example` and save as `.env`.

```
API_TOKEN="YOUR_ADMIN_API_TOKEN"
```

## Scripts

### purge_history.py
Purge history from all rooms older than 90 days.

`/_synapse/admin/v1/purge_history/`

## purge_empty_rooms.py
Purge all empty rooms.

`DELETE /_synapse/admin/v1/rooms`
