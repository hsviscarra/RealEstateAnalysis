with 

source as (

    select * from {{ source('staging', 'real_state_sales') }}

),

renamed as (

    select
        serial_number,
        list_year,
        date_recorded,
        town,
        address,
        assessed_value,
        sale_amount,
        sales_ratio,
        property_type,
        residential_type

    from source

)

select * from renamed
