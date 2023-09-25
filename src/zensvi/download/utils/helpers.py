import osmnx as ox

def standardize_column_names(df):
    longitude_variants = ['longitude', 'long', 'lon', 'lng', "x"]
    latitude_variants = ['latitude', 'lat', 'lt', "y"]
    # convert all column names to lowercase
    df.columns = [col.lower() for col in df.columns]      
    for col in df.columns:
        if col in longitude_variants:
            df.rename(columns={col: 'longitude'}, inplace=True)
        elif col in latitude_variants:
            df.rename(columns={col: 'latitude'}, inplace=True)
    return df

def create_buffer_gdf(gdf, buffer_distance):
    if gdf.crs == None:
        gdf = gdf.set_crs("EPSG:4326")
    
    if gdf.crs.is_projected == False:
        gdf = ox.projection.project_gdf(gdf)
    
    # Buffer the points by buffer_distance
    gdf['geometry'] = gdf.buffer(buffer_distance)
    
    # Project the GeoDataFrame back to EPSG:4326
    gdf = gdf.to_crs('EPSG:4326')
    
    return gdf