
import os
from supabase import create_client

supabase = create_client(
    os.environ["SUPABASE_URL"],
    os.environ["SUPABASE_PUBLISHABLE_KEY"]
)

response = (
    supabase.table("stock_records")
    .select("*")
    .limit(20)
    .execute()
)

for row in response.data:
    print(row)
