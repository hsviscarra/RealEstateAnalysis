{{
    config(
        materialized='table'
    )
}}

with aggregate_data as (
    select * from {{ ref('facts_rs') }}
)
    select
        sum(sale_amount) as sales_per_year,
        count(real_estate_id) as deals_per_year,
    from aggregate_data
    group by list_year, town




