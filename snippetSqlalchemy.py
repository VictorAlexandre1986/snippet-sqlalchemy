{

	"sqlalchemy select all": {
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
	"sqlalchemy select all limit": {
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
	"sqlalchemy select order by": {
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
	"sqlalchemy select order by limit": {
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
	"sqlalchemy select id": {
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
	"sqlalchemy select campo": {
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
	"sqlalchemy select campo limit": {
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
	"sqlalchemy select campo order by": {
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
	"sqlalchemy select campo order by limit": {
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
	"sqlalchemy select all distinct": {
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
	"sqlalchemy select all distinct limit": {
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
	"sqlalchemy select distinct": {
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
	"sqlalchemy select distinct limit": {
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
	"sqlalchemy select all between": {
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
	"sqlalchemy select all between limit": {
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
	"sqlalchemy select id between": {
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
	"sqlalchemy select id between limit": {
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
	"sqlalchemy select id between distinct": {
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
	"sqlalchemy select id between distinct limit": {
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
	"sqlalchemy select all between distinct": {
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
	"sqlalchemy select all between distinct limit": {
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
	"sqlalchemy insert": {
		"scope": "python",
		"prefix": "SQLAlchemyinsertTable",
		"body": [
			"def Create(data:dict):",
			"\ttry:",

			"\t\tnovo_cadastro = Tabela(",

			"\t\t\tnome=data['nome'],",

			"\t\t\tdataNascimento=data['dataNascimento'],",

			"\t\t)",

			"\t\tsession.add_all([novo_cadastro])",

			"\t\tsession.commit()",

			"\t\tsession.close()",

			"\t\treturn novo_cadastro",
			
			"\texcept Exception as e:",
			
			"\t\tprint(e)",
			
			"\t\tsession.rollback()",

		],
		"description": "Cria um exemplo de cadastro"
	},
	"sqlalchemy insert um para muitos": {
		"scope": "python",
		"prefix": "SQLAlchemyinsertTable1XN",
		"body": [
			"def Create(data:dict):",
			"\trua = session.query(Tabela2).filter(Tabela2.id=data['id']).one_or_none()",
			"",
			"\ttry:",

			"\t\tnovo_cadastro = Tabela(",

			"\t\t\tnome=data['nome'],",

			"\t\t\tdataNascimento=data['dataNascimento'],",

			"\t\t\tenderecao=rua",

			"\t\t)",

			"\t\tsession.add_all([novo_cadastro])",

			"\t\tsession.commit()",

			"\t\tsession.close()",

			"\t\treturn novo_cadastro",
			"",
			"\texcept Exception as e:",
	
			"\t\tprint(e)",
	
			"\t\tsession.rollback()",

		],
		"description": "Cria um exemplo de cadastro 1xM"
	},
	"sqlalchemy apagar": {
		"scope": "python",
		"prefix": "SQLAlchemyDelete",
		"body": [
			"def Delete(id:int):",
			"\ttry:",
			"\t\trua = session.query(Tabela).filter(Tabela.id=id).one_or_none()",
			
			"\t\tif rua:",

			"\t\t\tsession.delete(rua)",
			
			"\t\t\tsession.commit()",

			"\t\t\tsession.close()",

			"\t\t\treturn rua",
			"",
			"\texcept Exception as e:",
	
			"\t\tprint(e)",
	
			"\t\tsession.rollback()",

		],
		"description": "Cria um exemplo de delete"
	},
	"sqlalchemy atualizar": {
		"scope": "python",
		"prefix": "SQLAlchemyUpdate",
		"body": [
			"def Delete(id: int, data: dict):",
			"\ttry:",
			"\t\tcliente = session.query(Tabela).filter(Tabela.id=data['id']).one_or_none()",

			"\t\tif cliente:",


			"\t\t\tcliente.nome=data['nome']",
			
			"\t\t\tsession.commit()",

			"\t\t\tsession.close()",

			"\t\t\treturn cliente",
			"",
			"\texcept Exception as e:",
	
			"\t\tprint(e)",
	
			"\t\tsession.rollback()",

		],
		"description": "Cria um exemplo de update"
	},

}