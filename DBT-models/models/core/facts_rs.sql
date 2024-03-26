{{
    config(
        materialized='table'
    )
}}

with real_state_sales as (
    select *,
    'Connecticut' as state,
    from {{ ref('real_state_sales') }}
)
select * from real_state_sales
