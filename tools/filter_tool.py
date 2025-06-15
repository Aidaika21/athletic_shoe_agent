"""
Filter tool for refining shoe search results.
"""
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from data.shoes_database import search_shoes

class FilterInput(BaseModel):
    """Input for filtering athletic shoes."""
    brand: Optional[str] = Field(None, description="Brand name to filter by (Nike, Adidas, etc.)")
    type: Optional[str] = Field(None, description="Type of shoe (Running, Training, Basketball, etc.)")
    price_min: Optional[float] = Field(None, description="Minimum price")
    price_max: Optional[float] = Field(None, description="Maximum price")
    size: Optional[float] = Field(None, description="Shoe size")
    color: Optional[str] = Field(None, description="Color preference")

class FilterTool(BaseTool):
    """Tool for filtering athletic shoes by criteria."""
    name: str = "filter_athletic_shoes"
    description: str = "Filter athletic shoes by brand, type, price range, size, or color"
    args_schema: type[BaseModel] = FilterInput
    
    def _run(self, **kwargs) -> List[Dict[str, Any]]:
        """Run the filter tool on the shoes database."""
        # Remove None values to create a clean filter dict
        filters = {k: v for k, v in kwargs.items() if v is not None}
        results = search_shoes(filters=filters)
        return results
    
    async def _arun(self, **kwargs) -> List[Dict[str, Any]]:
        """Run the filter tool asynchronously."""
        return self._run(**kwargs)