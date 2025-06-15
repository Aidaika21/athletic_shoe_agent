"""
Search tool for querying the shoe database.
"""
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List

from data.shoes_database import search_shoes

class SearchInput(BaseModel):
    """Input for searching athletic shoes."""
    query: str = Field(..., description="The search query for athletic shoes")

class SearchTool(BaseTool):
    """Tool for searching athletic shoes by query text."""
    name: str = "search_athletic_shoes"
    description: str = "Search for athletic shoes by keywords or description"
    args_schema: type[BaseModel] = SearchInput
    
    def _run(self, query: str) -> List[Dict[str, Any]]:
        """Run the search tool on the shoes database."""
        results = search_shoes(query=query)
        return results
    
    async def _arun(self, query: str) -> List[Dict[str, Any]]:
        """Run the search tool asynchronously."""
        return self._run(query)