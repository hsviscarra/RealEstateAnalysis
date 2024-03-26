{% macro get_sales_categorization(var) -%}
case
    when {{ var }} > 1 then 'Over-valued'
    when {{ var }} = 1 then 'Equally valued'
    when {{ var }} < 1 then 'Undervalued'
    else 'Null'
end
{%- endmacro %}