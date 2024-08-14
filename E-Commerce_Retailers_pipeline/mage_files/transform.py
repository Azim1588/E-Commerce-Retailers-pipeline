import pandas as pd


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
  # Create Dimension Table: Customer_dim
  # Create Dimension Table: Customer_dim
    customer_dim = df[['CustomerID', 'CustomerName', 'Email', 'PhoneNumber']].drop_duplicates()
    customer_dim = customer_dim.reset_index(drop=True)
    customer_dim.columns = ['CustomerID', 'CustomerName', 'Email', 'PhoneNumber']
    # Create Dimension Table: Product
    product_dim = df[['ProductID', 'ProductName']].drop_duplicates().copy()
    customer_dim = customer_dim.reset_index(drop=True)
    product_dim.columns = ['ProductID', 'ProductName']  # Renaming to match the first code logic
    product_dim['Category'] = ''  # Placeholder for additional info
    product_dim['Brand'] = ''

    # Create Dimension Table: Date
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])
    date_dim = df[['OrderDate']].drop_duplicates().copy()
    date_dim.columns = ['Order_Date']  # Renaming to match the first code logic
    date_dim['Date_Key'] = date_dim['Order_Date'].dt.strftime('%Y%m%d')
    date_dim['Day'] = date_dim['Order_Date'].dt.day
    date_dim['Month'] = date_dim['Order_Date'].dt.month
    date_dim['Year'] = date_dim['Order_Date'].dt.year
    date_dim['Quarter'] = date_dim['Order_Date'].dt.to_period('Q').astype(str)


 # Create Dimension Table: Shipping Address
    shipping_address_dim = df[['ShippingAddress']].drop_duplicates().copy()
    shipping_address_dim.columns = ['ShippingAddress']  # Renaming to match the first code logic
    shipping_address_dim['Address_ID'] = shipping_address_dim.index + 1
    
    # Create Fact Table: Sales
# Map the Date to DateKey
    df = pd.merge(df, date_dim[['Order_Date', 'Date_Key']], left_on='OrderDate', right_on='Order_Date', how='left')
    
    # Map the Shipping Address to Address_ID
    df = pd.merge(df, shipping_address_dim[['ShippingAddress', 'Address_ID']], left_on='ShippingAddress', right_on='ShippingAddress', how='left')

# Select columns for Fact Table
    fact_table = df[['OrderID', 'CustomerID', 'ProductID', 'Quantity', 'Price', 'Date_Key', 'Address_ID']].copy()
    fact_table.columns = ['Order_ID', 'Customer_ID', 'Product_ID', 'Quantity', 'Price', 'Date_Key', 'Address_ID']  # Renaming to match the first code logic

    
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
