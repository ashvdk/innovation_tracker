from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_

from models.ProductSales import ProductSales
import pandas as pd

def companyOverviewFilters(db: Session = None, body = {}):
    try:
        print(body)
        if len(body) == 0:
            records = db.query(ProductSales).distinct(
            ProductSales.country, ProductSales.company, 
            ProductSales.segment, ProductSales.product_name, ProductSales.variant, ProductSales.color).all()
        else:
            filterCondition = []
            if "country" in body:
                filterCondition.append(ProductSales.country == body["country"])
            if "company" in body:
                filterCondition.append(ProductSales.company == body["company"])
            if "segment" in body:
                filterCondition.append(ProductSales.segment == body["segment"])
            if "product" in body:
                filterCondition.append(
                    ProductSales.product_name == body["product"])
            if "variant" in body:
                filterCondition.append(
                    ProductSales.variant == body["variant"])
            if "color" in body:
                filterCondition.append(
                    ProductSales.color == body["color"])
            print(filterCondition)
            records = db.query(ProductSales).filter(and_(*filterCondition)).distinct(
                ProductSales.country, ProductSales.company,
                ProductSales.segment, ProductSales.product_name, ProductSales.variant, ProductSales.color).all()
            
        records_df = pd.DataFrame([record.__dict__ for record in records])
        print(records_df.head(10))
        print(records_df["country"].unique())
        print(records_df["company"].unique())
        print(records_df["segment"].unique())
        print(records_df["product_name"].unique())
        print(records_df["variant"].unique())
        print(records_df["color"].unique())
        # {
        #     "country": records_df["country"].unique(),
        #     "company": records_df["company"].unique(),
        #     "segment": records_df["segment"].unique(),
        #     "product_name": records_df["product_name"],
        #     "variant": records_df["variant"],
        #     "color": records_df["color"]
        # }
        countries = [{"label": country, "value": country} for country in records_df["country"].unique()]
        companies = [{"label": company, "value": company}
                     for company in records_df["company"].unique()]
        segments = [{"label": segment, "value": segment}
                    for segment in records_df["segment"].unique()]
        products = [{"label": product, "value": product}
                    for product in records_df["product_name"].unique()]
        variants = [{"label": variant, "value": variant}
                    for variant in records_df["variant"].unique()]
        colors = [{"label": color, "value": color}
                  for color in records_df["color"].unique()]
        
        return {
            "country": countries,
            "company": companies,
            "segment": segments,
            "products": products,
            "variants": variants,
            "colors": colors 
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_products_overview(db: Session = None):
    try:
        # ProductSales.state.in_(states)
        products = db.query(ProductSales).filter(ProductSales.company == "SAMSUNG").all()
        tempAsdsArraySales = db.query(ProductSales).all()
        print(tempAsdsArraySales)
        data = [product.__dict__ for product in products]

        # Create DataFrame from the extracted data
        df = pd.DataFrame(data)
        diff_segments = {}
        diff_segments_rows = {}
        all_segments = df["segment"].unique()
        for segment in all_segments:
            diff_segments[segment] = 0
            diff_segments_rows[segment] = None

        for segment in diff_segments:
            all_rows = df[df["segment"] == segment]
            diff_segments_rows[segment] = all_rows
            diff_segments[segment] = all_rows["valusd"].sum()

        # smartphones = df[df["segment"] == "smartphones"]
        # tvs = df[df["segment"] == "tvs"]
        # tablets = df[df["segment"] == "tablets"]
        # laptops = df[df["segment"] == "laptops"]
        # smartwatch = df[df["segment"] == "smartwatch"]
        # earbuds = df[df["segment"] == "earbuds"]
        response = []
        all_products = {}
        for segment in diff_segments_rows:
            total_value = diff_segments_rows[segment].groupby(
                ['product_name'])['valusd'].sum()
            product_valusd = total_value.to_dict()
            for product in product_valusd:
                all_products[product] = {"sales": None, "units": None}
                product_valusd[product] = ((product_valusd[product]/diff_segments[segment])*100)
            diff_segments[segment] = {**product_valusd, "name": segment}
        # print(all_products)
        for eachProduct in  all_products:
            groupedData = df[df["product_name"] == eachProduct].groupby([
            'sales_year', 'quater'])
            quaterly_units = groupedData["units"].sum().to_dict()
            quaterly_sales = groupedData["valusd"].sum().to_dict()
            eachProductChartArray = []
            eachProductUnitArray = []
            for sales in quaterly_sales:
                eachProductChartArray.append({
                    "name": ''.join([str(sale) for sale in sales]),
                    "uv": quaterly_sales[sales]
                })
            for units in quaterly_units:
                eachProductUnitArray.append({
                    "name": ''.join([str(unit) for unit in units]),
                    "uv": quaterly_units[units]
                })
            all_products[eachProduct]["units"] = eachProductUnitArray
            all_products[eachProduct]["sales"] = eachProductChartArray
        return {"status": True, "data": {"sales_segment": diff_segments, "sales_products": all_products }, "error": ""}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    
    
