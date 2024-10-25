select brand, name, price, name, description, product_link
from(    
    select *, filter(product_colors, x -> x.colour_name='Honey') as colour_check
    from cosmetics
    )
where colour_check != array[] 
    and product_type = 'foundation' 
    and description like '%jojoba oil%'