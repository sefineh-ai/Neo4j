WITH "file:///data/nodes/accountant.csv" AS csv_file
LOAD CSV WITH HEADERS FROM csv_file AS row
WITH keys(row) AS headers, row
UNWIND headers AS header

MERGE (accountant:Accountant {id: row.id})
SET accountant[header] = row[header]

RETURN accountant
// ============================================================

// =====================================================================
WITH [ 
    'branch.csv', 
    'message.csv', 
    'accountant.csv', 
    'medio_pago.csv', 
    'currency.csv', 
    'provincia.csv', 
    'facturas.csv', 
    'profile.csv', 
    'lawyer.csv', 
    'quote_request.csv', 
    'impuesto_codigo.csv', 
    'subscription_plan.csv', 
    'cabys_code.csv', 
    'subscription_access_rule.csv', 
    'codigo_actividad.csv', 
    'condicion_venta.csv', 
    'connection.csv', 
    'impuesto_tarifa.csv', 
    'product_factura_template.csv',  
    'terminal.csv', 
    'canton.csv', 
    'subscription.csv', 
    'process_payment_request.csv', 
    'deleted_subscription.csv', 
    'factura_template.csv', 
    'message_status.csv', 
    'tilo_pay_modality.csv', 
    'client.csv', 
    'company_economic_activity.csv', 
    'linea_detalle.csv', 
    'quote_product.csv', 
    'conversation.csv', 
    'quote.csv', 
    'nota.csv', 
    'login_browser_session_data.csv', 
    'barrio.csv', 
    'functionality_resource.csv', 
    'company.csv', 
    'employee.csv', 
    'customer_feedback.csv', 
    'tax_payer_entity.csv', 
    'tilo_pay_plan.csv',
    'product.csv', 
    'connection_client.csv', 
    'distrito.csv', 
    'sandbox_invoice_sequence.csv', 
    'measure_unit.csv', 
    'profile_workflow_status.csv', 
    'currency_exchange_rate.csv'   
] AS csv_files

UNWIND csv_files AS csv_file
WITH csv_file, 
     REPLACE(LEFT(csv_file, SIZE(csv_file) - 4), '_', '') AS label
     
LOAD CSV WITH HEADERS FROM "file:///data/nodes/" + csv_file AS row
WITH keys(row) AS headers, row, label
UNWIND headers AS header
MERGE (entity:DataNode{id: row.id, type:label})
SET entity[header] = coalesce(row[header], 'null')
RETURN entity
// =============================================================

// =============================================================
LOAD CSV WITH HEADERS FROM "file:///data/relations/profile__accountants.csv" as row
MATCH (accountant:DataNode{id:row.start_id, type:"accountant"})
MATCH (profile:DataNode{id:row.end_id, type:"profile"})
MERGE (profile)-[:HAS_ROLE]->(accountant)
RETURN profile, accountant
// =============================================================

// CREATE A NEW RECORD FOR A SPECIFIC LABEL, NULL VALUE IS NOT ALLOWED
MATCH (profile:DataNode {type:"profile", id: "52"})
MERGE (accountant:DataNode {
  id: "2104",
  type: "accountant",
  accountant_status: "PENDING_REQUEST",
  client_status: "ACCEPTED",
  created_at: "2024-11-28 00:23:14.249394",
  email: "sefinehtesfa@gmail.com",
  first_name: "Sefineh",
  last_name: "Tesfa",
  accountant_profile_id: "202",
  assigned_profile_id: "208"
})
MERGE (profile)-[:HAS_ROLE]->(accountant)
RETURN accountant, profile
// =============================================================