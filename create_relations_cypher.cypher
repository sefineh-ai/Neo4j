WITH [ 
    "branch__terminals.csv",
    "nota__linea_detalles.csv",
    "canton__provincia.csv",
    "product__profile.csv",
    "client__profile.csv",
    "profile__accountants.csv",
    "codigo_actividad__nota.csv",
    "profile__company_role.csv",
    "company__barrio.csv",
    "profile__connection_client.csv",
    "company__codigo_actividad.csv",
    "profile__connections.csv",
    "company__favourite_codigo_actividads.csv",
    "profile__conversation.csv",
    "condicion_venta__nota.csv",
    "profile__lawyer.csv",
    "connection_client__provincia.csv",
    "profile__profile_company_roles.csv",
    "distrito__canton.csv",
    "profile__quote.csv",
    "facturas_linea_detalles.csv",
    "profile__tax_payer_entity.csv",
    "facturas__nota.csv",
    "quote_product__currency.csv",
    "factura_template__condicion_venta.csv",
    "quote__quote_product.csv",
    "factura_template_products.csv",
    "quote_request__cabys_codes.csv",
    "login_browser_session_data__profile.csv",
    "subscription_plan__currency.csv",
    "medio_pago__nota.csv",
    "terminal__branch.csv",
    "message__conversation.csv",
    "terminal_employee.csv",
    "message_status__profile.csv",
    "tilo_pay_plan__tilo_pay_modalities.csv"
] AS csv_files

UNWIND csv_files AS csv_file
WITH csv_file, [replace(split(csv_file, "__")[0], "_", ""), replace(split(csv_file, "__")[1], "_", "")] AS labels

CALL {
    WITH csv_file, labels
    LOAD CSV WITH HEADERS FROM 'file:///data/relations/' + csv_file AS row
    WITH row, labels
    WHERE row.start_id IS NOT NULL AND row.end_id IS NOT NULL AND row.type IS NOT NULL
    MERGE (startNode:`${labels[0]}` {id: row.start_id})
    MERGE (endNode:`${labels[1]}` {id: row.end_id})
    MERGE (startNode)-[r:ASSOCIATED_WITH]->(endNode)
    RETURN count(r) as relationship_count
}
RETURN "All relationships processed";
