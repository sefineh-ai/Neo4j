CREATE (user:User {
  firstName: "Sefineh", 
  lastName: "Tesfa", 
  email: "sefinehturing@gmail.com", 
  ccProfileEmail: true, 
  companyRole: "SENIOR_EMPLOYEE", 
  terminalCode: null, 
  profileId: 208, 
  branchId: 1652, 
  terminalId: 1752
})

CREATE (accountant:Profile {type: "ACCOUNTANT"})
CREATE (lawyer:Profile {type: "LAWYER"})
CREATE (employee:Profile {type: "EMPLOYEE"})

CREATE (user)-[:HAS_ROLE]->(accountant)
CREATE (user)-[:HAS_ROLE]->(lawyer)
CREATE (user)-[:HAS_ROLE]->(employee)
CREATE (company:Company {
  companyName: "NIMBU LAND HOLDING LIMITADA", 
  taxId: "3-102-823232", 
  economicActivity: "CONSTRUCCION DE EDIFICIOS", 
  province: "Cantón", 
  district: "Barrio", 
  address: "Edificio EBC piso 2", 
  emailForFactura: "sefinehturing@gmail.com"
})
CREATE (user)-[:HAS_COMPANY]->(company)
CREATE (client:Client {
  firstName: "Thomas", 
  lastName: "Garben", 
  email: "tom@pamipami.cr", 
  companyName: "Pami Factura"
})
CREATE (company)-[:HAS_CLIENT]->(client)

CREATE (employeeNode:Employee {
  firstName: "Sefineh", 
  lastName: "Tesfa", 
  email: "sefinehturing@gmail.com", 
  companyRole: "SENIOR_EMPLOYEE", 
  terminalCode: null, 
  profileId: 208, 
  branchId: 1652, 
  terminalId: 1752
})
CREATE (company)-[:HAS_EMPLOYEE]->(employeeNode)
CREATE (accountantNode:Accountant {
  firstName: "Sefineh", 
  lastName: "Tesfa", 
  email: "sefinehtesfa@gmail.com", 
  connectionType: "ACCOUNTANT", 
  type: "ACCOUNTANT", 
  profileId: 208
})

CREATE (company)-[:HAS_ACCOUNTANT]->(accountantNode)
CREATE (lawyerNode:Lawyer {
  firstName: "John", 
  lastName: "Doe", 
  email: "johndoe@gmail.com", 
  profileId: 209
})
CREATE (company)-[:HAS_LAWYER]->(lawyerNode)
CREATE (hacienda:Hacienda {
  haciendaUsername: "cpj-3-102-823232@stag.comprobanteselectronicos.go.cr", 
  haciendaPassword: "••••••••••", 
  haciendaCertPassword: "••••", 
  cryptographicKeyFile: "/files/crypto_key.pem"
})

CREATE (company)-[:HAS_HACIENDA]->(hacienda)
CREATE (invoice:QuoteInvoice {
  id: "12345", 
  type: "Invoice", 
  amount: 1000.0, 
  date: "2024-11-28"
})

CREATE (user)-[:IS_SENDER]->(invoice)
CREATE (client)-[:IS_RECEIVER]->(invoice)

CREATE (user2:User {
  firstName: "Jane", 
  lastName: "Doe", 
  email: "jane.doe@gmail.com", 
  ccProfileEmail: true, 
  companyRole: "JUNIOR_ACCOUNTANT", 
  terminalCode: null, 
  profileId: 209, 
  branchId: 1653, 
  terminalId: 1753
})

CREATE (accountant2:Profile {type: "ACCOUNTANT"})
CREATE (lawyer2:Profile {type: "LAWYER"})
CREATE (user2)-[:HAS_ROLE]->(accountant2)
CREATE (user2)-[:HAS_ROLE]->(lawyer2)

CREATE (user2)-[:HAS_COMPANY]->(company)
CREATE (user2)-[:IS_SENDER]->(invoice)
CREATE (client)-[:IS_RECEIVER]->(invoice)

CREATE (user2)-[:ASSOCIATED_WITH]->(client)
CREATE (user)-[:ASSOCIATED_WITH]->(client)
CREATE (user2)-[:ASSOCIATED_WITH]->(employeeNode)

CREATE (employeeNode)-[:ASSOCIATED_WITH]->(client)
CREATE (accountantNode)-[:ASSOCIATED_WITH]->(client)
CREATE (lawyerNode)-[:ASSOCIATED_WITH]->(client)

CREATE (lawyerNode)-[:COLLABORATES_WITH]->(accountantNode)
CREATE (accountantNode)-[:SUPERVISES]->(employeeNode)
CREATE (financialDoc:FinancialDocument {
  documentId: "FD001", 
  type: "Financial Report", 
  date: "2024-11-28", 
  amount: 5000.0
})

CREATE (client)-[:HAS_FINANCIAL_DOCUMENT]->(financialDoc)
CREATE (accountantNode)-[:MANAGES_FINANCIAL_DOCUMENT]->(financialDoc)
CREATE (user)-[:MANAGES_CLIENT_RELATIONSHIP]->(lawyerNode)
CREATE (user)-[:WORKS_ON]->(invoice)
CREATE (lawyerNode)-[:WORKS_WITH]->(hacienda)
CREATE (invoice)-[:PROCESSES_PAYMENT]->(hacienda)
CREATE (employeeNode)-[:PART_OF_TEAM]->(company)
CREATE (accountantNode)-[:APPROVED_BY]->(invoice)
