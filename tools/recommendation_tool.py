"""
Recommendation tool that suggests athletic shoes based on user preferences and activities.
"""
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

from data.shoes_database import search_shoes, get_all_shoes

class RecommendationInput(BaseModel):
    """Input for recommending athletic shoes."""
    activity: str = Field(..., description="Athletic activity the shoes will be used for (e.g., running, training, basketball)")
    user_description: str = Field(..., description="User description of their preferences, needs, or problems to solve")
    budget_max: Optional[float] = Field(None, description="Maximum budget for the shoes")
    preferred_brands: Optional[List[str]] = Field(None, description="List of preferred brands, if any")

class RecommendationTool(BaseTool):
    """Tool for recommending athletic shoes based on user preferences and activities."""
    name: str = "recommend_athletic_shoes"
    description: str = "Get personalized athletic shoe recommendations based on activities and preferences"
    args_schema: type[BaseModel] = RecommendationInput
    
    def _run(
        self, 
        activity: str, 
        user_description: str,
        budget_max: Optional[float] = None,
        preferred_brands: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """Run the recommendation tool to suggest shoes."""
        # Start with all shoes or a filtered subset based on activity
        results = search_shoes(query=activity)
        
        # Apply budget constraint if provided
        if budget_max is not None and budget_max > 0:
            results = [shoe for shoe in results if shoe['price'] <= budget_max]
        
        # Apply brand preference if provided
        if preferred_brands and len(preferred_brands) > 0:
            preferred_brands_lower = [b.lower() for b in preferred_brands]
            # Only filter by brand if preferences were given
            results = [shoe for shoe in results if shoe['brand'].lower() in preferred_brands_lower]
            
        # Sort by relevance - in a real app, this would use a proper ranking algorithm
        # For now, we'll just sort by rating as a proxy for quality
        results.sort(key=lambda x: x['rating'], reverse=True)
        
        # Return top recommendations (limited to 5 for simplicity)
        return results[:5]
    
    async def _arun(
        self, 
        activity: str, 
        user_description: str,
        budget_max: Optional[float] = None,
        preferred_brands: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """Run the recommendation tool asynchronously."""
        return self._run(activity, user_description, budget_max, preferred_brands)