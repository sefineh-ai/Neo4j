import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=int(os.getenv("DB_PORT"))
)

cursor = connection.cursor()
tables = [
    "accountant", "accountant_seq", "bank_transaction_raw_data", "bank_transaction_raw_data_seq", 
    "barrio", "branch", "branch_seq", "branch_terminals", "cabys_code", "cabys_code_seq", 
    "cabys_reduced", "cabys_reduced_seq", "canton", "client", "client_seq", "codigo_actividad", 
    "codigo_actividad_seq", "company", "company_codigo_actividad", "company_economic_activity", 
    "company_economic_activity_seq", "company_favourite_codigo_actividads", "company_seq", 
    "condicion_venta", "condicion_venta_seq", "connection", "connection_client", "connection_client_seq", 
    "connection_seq", "conversation", "conversation_profile", "currency", "currency_exchange_rate", 
    "currency_exchange_rate_seq", "currency_seq", "customer_feedback", "customer_feedback_seq", 
    "deleted_subscription", "deleted_subscription_seq", "distrito", "employee", "employee_seq", 
    "factura_template", "factura_template_products", "factura_template_seq", "facturas", 
    "facturas_linea_detalles", "facturas_notas", "facturas_seq", "favorite_clients", 
    "flyway_schema_history", "functionality_resource", "functionality_resource_seq", "hacienda_credentials", 
    "hacienda_credentials_seq", "impuesto_codigo", "impuesto_codigo_seq", "impuesto_tarifa", 
    "impuesto_tarifa_seq", "lawyer", "lawyer_seq", "linea_detalle", "linea_detalle_seq", 
    "login_browser_session_data", "login_browser_session_data_seq", "measure_unit", "measure_unit_seq", 
    "medio_pago", "medio_pago_seq", "message", "message_status", "nota", "nota_linea_detalles", "nota_seq", 
    "process_payment_request", "process_payment_request_seq", "product", "product_factura_template", 
    "product_factura_template_seq", "product_seq", "profile", "profile_accountants", "profile_company_role", 
    "profile_company_role_seq", "profile_connections", "profile_lawyers", "profile_profile_company_roles", 
    "profile_roles", "profile_seq", "profile_workflow_status", "profile_workflow_status_seq", "provincia", 
    "quote", "quote_product", "quote_product_seq", "quote_quote_products", "quote_request", 
    "quote_request_cabys_codes", "quote_request_seq", "quote_seq", "sandbox_invoice_sequence", 
    "sandbox_invoice_sequence_seq", "subscription", "subscription_access_rule", 
    "subscription_access_rule_functionality_resource_list", "subscription_access_rule_seq", "subscription_plan", 
    "subscription_plan_seq", "subscription_seq", "tax_payer_entity", "tax_payer_entity_seq", "terminal", 
    "terminal_seq", "tilo_pay_modality", "tilo_pay_modality_seq", "tilo_pay_plan", "tilo_pay_plan_seq", 
    "tilo_pay_plan_tilo_pay_modalities"
]

output_dir = '/home/sefineh/Desktop/Neo4j/data/'
for table in tables:
    try:
        query = f"SELECT * FROM {table}"
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        output_path = os.path.join(output_dir, f"{table}.csv")

        with open(output_path, mode='w', newline='', encoding='utf-8') as file:
            file.write(','.join(columns) + '\n')
            for row in rows:
                file.write(','.join(str(value) if value is not None else '' for value in row) + '\n')

        print(f"Successfully exported {table} to {output_path}")

    except Exception as e:
        print(f"Error exporting table {table}: {e}")

cursor.close()
connection.close()
