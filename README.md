# Neo4j Graph Database Project

A comprehensive Neo4j graph database project for managing business and financial data with complex relationships between entities such as profiles, companies, invoices, products, and more.

## 🎯 Project Overview

This project provides a complete solution for:
- **Data Migration**: Exporting data from MySQL databases to Excel format
- **Graph Database Setup**: Creating and managing Neo4j graph database with Docker
- **Data Import**: Loading CSV data into Neo4j nodes and relationships
- **Advanced Querying**: Complex Cypher queries for data analysis and filtering

## 🏗️ Architecture

The project handles various business entities including:
- **Profiles & Users**: User management and authentication
- **Companies & Organizations**: Business entity management
- **Financial Data**: Invoices, quotes, payments, and transactions
- **Products & Services**: Product catalog and pricing
- **Geographic Data**: Provinces, cantons, districts, and neighborhoods
- **Tax & Legal**: Tax codes, activities, and compliance data

## 📁 Project Structure

```
Neo4j/
├── data/                          # Data storage
│   ├── nodes/                     # CSV files for node creation
│   ├── relations/                 # CSV files for relationship creation
│   ├── excel/                     # Exported Excel files
│   └── csv/                       # Raw CSV data
├── neo4j_env/                     # Python virtual environment
├── import/                        # Neo4j import directory
├── logs/                          # Neo4j logs
├── plugins/                       # Neo4j plugins
├── access.py                      # MySQL to Excel data export
├── create_nodes.py                # Create nodes in Neo4j
├── create_relations.py            # Create relationships in Neo4j
├── relation.py                    # Relationship processing utilities
├── indexing.py                    # Database indexing utilities
├── urls.py                        # URL management for data sources
├── docker-compose.yml             # Neo4j Docker configuration
├── .env                          # Environment variables
└── .gitignore                    # Git ignore rules
```

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- Python 3.8+
- MySQL database access
- Neo4j database

### 1. Environment Setup

Create a `.env` file with your configuration:

```bash
# MySQL Database Configuration
DB_HOST=your_mysql_host
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_NAME=your_database_name
DB_PORT=3306

# Neo4j Configuration
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=password
```

### 2. Start Neo4j Database

```bash
# Start Neo4j with Docker Compose
docker-compose up -d

# Access Neo4j Browser at: http://localhost:7474
# Default credentials: neo4j/password
```

### 3. Install Python Dependencies

```bash
# Create virtual environment
python -m venv neo4j_env
source neo4j_env/bin/activate  # On Windows: neo4j_env\Scripts\activate

# Install dependencies
pip install neo4j python-dotenv mysql-connector-python openpyxl requests pandas numpy
```

### 4. Data Export from MySQL

```bash
# Export MySQL data to Excel files
python access.py
```

### 5. Create Nodes in Neo4j

```bash
# Import CSV data as nodes
python create_nodes.py
```

### 6. Create Relationships

```bash
# Create relationships between nodes
python create_relations.py
```

## 📊 Data Models

### Main Node Types

- **Profile**: User profiles and authentication data
- **Company**: Business entities and organizations
- **Product**: Products and services catalog
- **Factura**: Invoice and billing data
- **Quote**: Quote and pricing information
- **Message**: Communication and messaging data
- **Connection**: Network connections and relationships

### Key Relationships

- `PROFILE__COMPANY_ROLE`: User roles within companies
- `PRODUCT__PROFILE`: Product ownership and management
- `FACTURAS__LINEA_DETALLES`: Invoice line items
- `MESSAGE__CONVERSATION`: Message threading
- `COMPANY__BARRIO`: Company location data

## 🔍 Advanced Queries

The project includes advanced Cypher queries for complex data analysis:

### Filtering and Search

```cypher
// Advanced filtering examples available in advanced_filtering.cypher
MATCH (p:Profile)-[:PROFILE__COMPANY_ROLE]->(cr:Company_role)
WHERE p.email CONTAINS '@company.com'
RETURN p, cr
```

### Data Analysis

```cypher
// Complex relationship analysis
MATCH (c:Company)-[:COMPANY__BARRIO]->(b:Barrio)
MATCH (c)-[:COMPANY__CODIGO_ACTIVIDAD]->(ca:Codigo_actividad)
RETURN c.name, b.name, ca.description
```

## 🛠️ Utilities

### Data Processing

- **`access.py`**: MySQL to Excel data export with character sanitization
- **`create_ids.py`**: Generate unique identifiers for data
- **`prepare_relations_for_import.py`**: Prepare relationship data for import
- **`sheet_to_csv.py`**: Convert Excel sheets to CSV format

### Database Management

- **`indexing.py`**: Create database indexes for performance
- **`urls.py`**: Manage data source URLs and file locations

## 🔧 Configuration

### Docker Configuration

The `docker-compose.yml` includes:
- Neo4j database with APOC plugins
- File import/export capabilities
- Volume mounts for data persistence
- Port mappings (7474 for browser, 7687 for Bolt)

### Environment Variables

Key configuration options:
- Database connection parameters
- Neo4j authentication
- File paths and URLs
- Processing options

## 📈 Performance Optimization

- Database indexing for frequently queried properties
- Batch processing for large datasets
- Connection pooling for database operations
- Error handling and retry mechanisms

## 🐛 Troubleshooting

### Common Issues

1. **Connection Errors**: Verify Neo4j is running and credentials are correct
2. **Import Failures**: Check CSV file format and data consistency
3. **Memory Issues**: Adjust Neo4j memory settings for large datasets
4. **Permission Errors**: Ensure proper file permissions for data directories

### Logs

Check Neo4j logs in the `logs/` directory for detailed error information.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- [Neo4j Documentation](https://neo4j.com/docs/)
- [Cypher Query Language](https://neo4j.com/docs/cypher-manual/current/)
- [APOC Procedures](https://neo4j.com/docs/apoc/current/)

## 📞 Support

For questions and support, please open an issue in the GitHub repository. 