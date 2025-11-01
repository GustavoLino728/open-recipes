import requests
from typing import Dict, Optional, List
from app.config import Config
from app.utils import logger

class APIService:
    """Serviço para comunicação com a API de receitas"""
    
    def __init__(self):
        self.base_url = Config.API_BASE_URL
        self.timeout = 30
    
    def _normalize_response(self, response_data: Dict) -> Dict:
        """
        Normaliza a resposta da API externa
        Converte 'items' para 'data' para manter consistência
        """
        if 'items' in response_data and 'data' not in response_data:
            response_data['data'] = response_data.pop('items')
            logger.info(f"✅ Resposta normalizada: {len(response_data['data'])} receitas")
        
        return response_data
        
    def _make_request(self, method: str, endpoint: str, params: Optional[Dict] = None, 
                      data: Optional[Dict] = None, headers: Optional[Dict] = None) -> Dict:
        """Método genérico para fazer requisições HTTP"""
        url = f"{self.base_url}{endpoint}"
        
        try:
            logger.info(f"Fazendo requisição {method} para {url}")
            
            response = requests.request(
                method=method,
                url=url,
                params=params,
                json=data,
                headers=headers,
                timeout=self.timeout
            )
            
            response.raise_for_status()
            response_data = response.json()
            
            # Normalizar a resposta
            normalized_data = self._normalize_response(response_data)
            
            return normalized_data
            
        except requests.exceptions.Timeout:
            logger.error(f"Timeout na requisição para {url}")
            raise ConnectionError("A requisição demorou muito tempo")
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro na requisição: {str(e)}")
            raise ConnectionError(f"Erro ao conectar com a API: {str(e)}")
    
    def get_todas_receitas(self, page: int = 1, limit: int = 10) -> Dict:
        """Busca todas as receitas com paginação"""
        params = {'page': page, 'limit': limit}
        return self._make_request('GET', '/receitas/todas', params=params)
    
    def get_receita_por_id(self, receita_id: int) -> Dict:
        """Busca receita específica por ID"""
        return self._make_request('GET', f'/receitas/{receita_id}')
    
    def get_receitas_por_tipo(self, tipo: str) -> Dict:
        """Busca receitas por tipo (doce, salgado, agridoce)"""
        if tipo not in ['doce', 'salgado', 'agridoce']:
            raise ValueError("Tipo deve ser: doce, salgado ou agridoce")
        return self._make_request('GET', f'/receitas/tipo/{tipo}')
    
    def get_receitas_por_descricao(self, descricao: str, page: int = 1, limit: int = 10) -> Dict:
        """Busca receitas por descrição/nome"""
        if not descricao or len(descricao.strip()) == 0:
            raise ValueError("Descrição não pode ser vazia")
        
        params = {
            'descricao': descricao,
            'page': page,
            'limit': limit
        }
        return self._make_request('GET', '/receitas/descricao', params=params)
    
    def get_ingredientes_por_receita(self, receita_id: int) -> Dict:
        """Busca ingredientes de uma receita específica"""
        return self._make_request('GET', f'/receitas/ingredientes/{receita_id}')
    
    def buscar_por_ingredientes(self, ingredientes: List[str], page: int = 1, limit: int = 10) -> Dict:
        """
        Busca receitas que contenham os ingredientes informados
        Como a API não tem endpoint específico, vamos buscar por cada ingrediente
        e consolidar os resultados
        """
        if not ingredientes or len(ingredientes) == 0:
            raise ValueError("Lista de ingredientes não pode ser vazia")
        
        # Buscar receitas para cada ingrediente
        all_receitas = {}
        
        for ingrediente in ingredientes:
            try:
                resultado = self.get_receitas_por_descricao(ingrediente, page=1, limit=50)
                
                if 'data' in resultado:
                    for receita in resultado['data']:
                        receita_id = receita.get('id')
                        if receita_id:
                            # Se já existe, aumenta o score (quantos ingredientes possui)
                            if receita_id in all_receitas:
                                all_receitas[receita_id]['match_score'] += 1
                            else:
                                receita['match_score'] = 1
                                all_receitas[receita_id] = receita
                                
            except Exception as e:
                logger.warning(f"Erro ao buscar ingrediente '{ingrediente}': {str(e)}")
                continue
        
        # Ordenar por match_score (receitas com mais ingredientes primeiro)
        receitas_ordenadas = sorted(
            all_receitas.values(), 
            key=lambda x: x['match_score'], 
            reverse=True
        )
        
        # Aplicar paginação manual
        start = (page - 1) * limit
        end = start + limit
        receitas_paginadas = receitas_ordenadas[start:end]
        
        total_count = len(receitas_ordenadas)
        page_count = (total_count + limit - 1) // limit
        
        return {
            'data': receitas_paginadas,
            'meta': {
                'page': page,
                'limit': limit,
                'itemCount': len(receitas_paginadas),
                'totalItems': total_count,
                'pageCount': page_count,
                'hasPreviousPage': page > 1,
                'hasNextPage': page < page_count
            }
        }