SELECT seller_id,
      count(*) AS frequencia,
      sum(price) AS valor

FROM tb_order_items
GROUP BY 1
