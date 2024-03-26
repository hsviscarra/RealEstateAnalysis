{{
    config(
        materialized='view'
    )
}}

with 

source as (

    select *,
    row_number() over(partition by serial_number) as rn
    from {{ source('staging', 'real_state_sales') }}
    where serial_number is not null

),

renamed as (

    select
        {{ dbt_utils.generate_surrogate_key(['serial_number', 'date_recorded']) }} as real_estate_id,
        serial_number,
        list_year,
        date_recorded,
        town,
        address,
        assessed_value,
        sale_amount,
        sales_ratio,
        {{ get_sales_categorization('sales_ratio') }} as appraisal_value_cat, 
        property_type,
        residential_type
    from source

)

select * from renamed

