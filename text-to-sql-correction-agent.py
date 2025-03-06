import os

from dotenv import load_dotenv
from huggingface_hub import login
from smolagents import OpenAIServerModel
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    Float,
    insert,
    inspect,
    text,
)
from smolagents import tool
from smolagents import CodeAgent, HfApiModel

load_dotenv()
login(token=os.getenv("HF_TOKEN"))

engine = create_engine("sqlite:///:memory:")
metadata_obj = MetaData()


table_name = "receipts"
receipts = Table(
    table_name,
    metadata_obj,
    Column("receipt_id", Integer, primary_key=True),
    Column("customer_name", String(16), primary_key=True),
    Column("price", Float),
    Column("tip", Float),
)

metadata_obj.create_all(engine)

rows = [
    {"receipt_id": 1, "customer_name": "Alan Payne", "price": 12.06, "tip": 1.20},
    {"receipt_id": 2, "customer_name": "Alex Mason", "price": 23.86, "tip": 0.24},
    {"receipt_id": 3, "customer_name": "Woodrow Wilson", "price": 53.43, "tip": 5.43},
    {"receipt_id": 4, "customer_name": "Margaret James", "price": 21.11, "tip": 1.00},
]

for row in rows:
    stmt = insert(receipts).values(**row)
    with engine.begin() as connection:
        cursor = connection.execute(stmt)

# with engine.connect() as con:
#     rows = con.execute(text("""SELECT * from receipts"""))
#     for row in rows:
#         print(row)

table_name = "waiters"
receipts = Table(
    table_name,
    metadata_obj,
    Column("receipt_id", Integer, primary_key=True),
    Column("waiter_name", String(16), primary_key=True),
)
metadata_obj.create_all(engine)

rows = [
    {"receipt_id": 1, "waiter_name": "Corey Johnson"},
    {"receipt_id": 2, "waiter_name": "Michael Watts"},
    {"receipt_id": 3, "waiter_name": "Michael Watts"},
    {"receipt_id": 4, "waiter_name": "Margaret James"},
]
for row in rows:
    stmt = insert(receipts).values(**row)
    with engine.begin() as connection:
        cursor = connection.execute(stmt)

@tool
def sql_engine(query: str) -> str:
    """
    Allows you to perform SQL queries on the table. Beware that this tool's output is a string representation of the execution output.
    
    It can use the following tables:

    Table 'receipts':
    Columns:
    - receipt_id: INTEGER
    - customer_name: VARCHAR(16)
    - price: FLOAT
    - tip: FLOAT

    Table 'waiters':
    Columns:
    - receipt_id: INTEGER
    - waiter_name: VARCHAR(16)

    Args:
        query: The query to perform. This should be correct SQL.
    """
    output = ""
    with engine.connect() as con:
        rows = con.execute(text(query))
        for row in rows:
            output += "\n" + str(row)
    return output

model = OpenAIServerModel(
    model_id=os.getenv("OPENAI_API_MODEL_ID"),
    api_base=os.getenv("OPENAI_API_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

updated_description = """Allows you to perform SQL queries on the table. Beware that this tool's output is a string representation of the execution output.
It can use the following tables:"""

inspector = inspect(engine)
for table in ["receipts", "waiters"]:
    columns_info = [(col["name"], col["type"]) for col in inspector.get_columns(table)]

    table_description = f"Table '{table}':\n"

    table_description += "Columns:\n" + "\n".join([f"  - {name}: {col_type}" for name, col_type in columns_info])
    updated_description += "\n\n" + table_description

# print(updated_description)

sql_engine.description = updated_description

agent = CodeAgent(
    tools=[sql_engine],
    model=model,
)


agent.run("Which waiter got more total money from tips?")




