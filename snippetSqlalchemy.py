{

	"select all": {
		"scope": "python",
		"prefix": "selectAll",
		"body": [
			"def getall():",
			"\tresult = session.query('tabela$1').all()",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(lista_itens)",
			""
		],
		"description": "Cria um select all"
	},
	"select all limit": {
		"scope": "python",
		"prefix": "selectAllLimit",
		"body": [
			"def getallLimit(limit:int, offset:int):",
			"\tresult = session.query('tabela$1').all().limit(limit).offset(offset)",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(lista_itens)",
			""
		],
		"description": "Cria um select all com limit"
	},
	"select order by": {
		"scope": "python",
		"prefix": "selectAllOrderBy",
		"body": [
			"def getallOrderBy():",
			"\tresult = session.query('tabela$1').all().order_by('$2tabela.$3campo.desc(),$4tabela.$5campo.asc()')",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(lista_itens)",
			""
		],
		"description": "Cria um select all com order by"
	},
	"select order by limit": {
		"scope": "python",
		"prefix": "selectAllOrderByLimit",
		"body": [
			"def getallOrderByLimit(limit:int, offoset:int):",
			"\tresult = session.query('tabela$1').all().order_by('$2tabela.$3campo.desc(),$4tabela.$5campo.asc()').limit(limit).offset(offset)",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(lista_itens)",
			""
		],
		"description": "Cria um select all com order by e limit"
	},
	"select id": {
		"scope": "python",
		"prefix": "selectId",
		"body": [
			"def getId(id: int):",
			"\tresult = session.query('$1tabela').filter('$2tabela'.id='id$3')",
			"",
			"\tsession.close()",
			"",
			"\treturn(result)",
			""
		],
		"description": "Cria um select por id"
	},
	"select campo": {
		"scope": "python",
		"prefix": "selectCampo",
		"body": [
			"def getId(campo: str):",
			"\tresult = session.query('$1tabela').filter('$2tabela'.campo='campo$3')",
			"",
			"\tsession.close()",
			"",
			"\treturn(result)",
			""
		],
		"description": "Cria um select por id "
	},
	"select campo limit": {
		"scope": "python",
		"prefix": "selectCampoLimit",
		"body": [
			"def getIdLimit(campo: str, limit: int, offset:int):",
			"\tresult = session.query('$1tabela').filter('$2tabela'.campo='campo$3').limit(limit).offset(offset)",
			"",
			"\tsession.close()",
			"",
			"\treturn(result)",
			""
		],
		"description": "Cria um select por campo  com limit"
	},
	"select campo order by": {
		"scope": "python",
		"prefix": "selectIdOrderBy",
		"body": [
			"def getIdOrderBy(campo: str):",
			"\tresult = session.query('$1tabela').filter('$2tabela'.campo='campo$3').order_by(('$2tabela.$3campo.desc(),$4tabela.$5campo.asc()')",
			"",
			"\tsession.close()",
			"",
			"\treturn(result)",
			""
		],
		"description": "Cria um select por id com order by"
	},
	"select campo order by limit": {
		"scope": "python",
		"prefix": "selectIdOrderByLimit",
		"body": [
			"def getIdOrderByLimit(campo: str, limit: int, offset: int):",
			"\tresult = session.query('$1tabela').filter('$2tabela'.campo='campo$3').order_by(('$2tabela.$3campo.desc(),$4tabela.$5campo.asc()').limit(limit).offset(offset)",
			"",
			"\tsession.close()",
			"",
			"\treturn(result)",
			""
		],
		"description": "Cria um select por id com order by e limit"
	},
	"select all distinct": {
		"scope": "python",
		"prefix": "selectAllDistinct",
		"body": [
			"def getAllUnique():",
			"\tresult = session.query('$1tabela.campo$2').all().distinct()",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(lista_itens)",
			""
		],
		"description": "Cria um select all com valores unicos"
	},
	"select all distinct limit": {
		"scope": "python",
		"prefix": "selectAllDistinctLimit",
		"body": [
			"def getAllDistinctLimit():",
			"\tresult = session.query('$1tabela.campo$2').all().limit(limit).offset(offset).distinct()",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(result)",
			""
		],
		"description": "Cria um select all com valores unicos com limite"
	},
	"select distinct": {
		"scope": "python",
		"prefix": "selectDistinct",
		"body": [
			"def getUnique(campo: str):",
			"\tresult = session.query('$1tabela.$2campo').filter('$3tabela'.campo=campo).distinct()",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(lista_itens)",
			""
		],
		"description": "Cria um select com filter e distinct"
	},
	"select distinct limit": {
		"scope": "python",
		"prefix": "selectDistinctLimit",
		"body": [
			"def getDistinctLimit(campo: str, limite: int, offset: int):",
			"\tresult = session.query('$1tabela.$2campo').filter('$3tabela'.campo=campo).limite(limite).offset(offset).distinct()",
			"",
			"\tsession.close()",
			"",
			"\treturn(result)",
			""
		],
		"description": "Cria um select com filter e distinct e limit"
	},
	"select all between": {
		"scope": "python",
		"prefix": "selectAllBetween",
		"body": [
			"def getBetween():",
			"\tresult = session.query('$1tabela').filter('$2Tabela.$3campo.between($4valorInicial,$5valorFinal)').all()",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(lista_itens)",
			""
		],
		"description": "Cria um select all com between"
	},
	"select all between limit": {
		"scope": "python",
		"prefix": "selectAllBetweenLimit",
		"body": [
			"def getBetweenLimit(limit: int, offset: int):",
			"\tresult = session.query('$1tabela').filter('$2Tabela.$3campo.between($4valorInicial,$5valorFinal)').all().limit(limit).offset(offset)",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(lista_itens)",
			""
		],
		"description": "Cria um select all com between com limit"
	},
	"select id between": {
		"scope": "python",
		"prefix": "selectIdBetween",
		"body": [
			"def getBetween(campo: str):",
			"\tresult = session.query('$1tabela').filter('$2Tabela.$3campo.between($4valorInicial,$5valorFinal)').filter($6Tabela.$7campo=campo)",
			"",
			"\tsession.close()",
			"",
			"\treturn(result)",
			""
		],
		"description": "Cria um select filtrado com between"
	},
	"select id between limit": {
		"scope": "python",
		"prefix": "selectIdBetweenLimit",
		"body": [
			"def getBetweenLimit(campo: str, limit:int, offset: int):",
			"\tresult = session.query('$1tabela').filter('$2Tabela.$3campo.between($4valorInicial,$5valorFinal)').filter($6Tabela.$7campo=campo).limit(limit).offset(offset)",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(lista_itens)",
			""
		],
		"description": "Cria um select filtrado com between com limit"
	},
	"select id between distinct": {
		"scope": "python",
		"prefix": "selectIdBetweenDistinct",
		"body": [
			"def getIdBetweenDistinct(valorInicial:str, valorFinal: str, campo: str):",
			"\tresult = session.query('$1tabela').filter('$2Tabela.$3campo.between($4valorInicial,$5valorFinal)').filter($6Tabela.$7campo=campo).distinct()",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(lista_itens)",
			""
		],
		"description": "Cria um select filtrado com between e distinct"
	},
	"select id between distinct limit": {
		"scope": "python",
		"prefix": "selectIdBetweenDistinctLimit",
		"body": [
			"def getIdBetweenDistinctLimit(valorInicial:str, valorFinal: str, campo: str, limit: int, offset:int):",
			"\tresult = session.query('$1tabela').filter('$2Tabela.$3campo.between($4valorInicial,$5valorFinal).limit(limit).offset(offset)').filter($6Tabela.$7campo=campo).distinct()",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(lista_itens)",
			""
		],
		"description": "Cria um select filtrado com between e distinct com limit"
	},
	"select all between distinct": {
		"scope": "python",
		"prefix": "selectAllBetweenDistinct",
		"body": [
			"def getBetweenDistinct(valorInicial: str, valorFinal: str):",
			"\tresult = session.query('$1tabela').filter('$2Tabela.$3campo.between($4valorInicial,$5valorFinal)').distinct()",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(lista_itens)",
			""
		],
		"description": "Cria um select all com between e distinct"
	},
	"select all between distinct limit": {
		"scope": "python",
		"prefix": "selectAllBetweenDistinctLimit",
		"body": [
			"def getBetweenDistinctLimit(valorInicial: str, valorFinal: str, limit: int, offset: int):",
			"\tresult = session.query('$1tabela').filter('$2Tabela.$3campo.between($4valorInicial,$5valorFinal)').limit(limit).offset(offset).distinct()",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(lista_itens)",
			""
		],
		"description": "Cria um select all com between e distinct com limit"
	},
}