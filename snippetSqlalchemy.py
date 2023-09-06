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
	"sqlalchemy select in": {
		"scope": "python",
		"prefix": "selectIn",
		"body": [
			"def getIn():",
			"",
			"\tnomes_a_pesquisar = ['Alice', 'Bob', 'Charlie']",
			"",
			"\tresult = session.query(Pessoa).filter(Pessoa.nome.in_(nomes_a_pesquisar)).all()",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(lista_itens)",
			""
		],
		"description": "Cria um select usando in"
	},
	"sqlalchemy select and": {
		"scope": "python",
		"prefix": "selectAnd",
		"body": [
			"def getAnd(adultos,criancas):",
			"",
			"\tresult = session.query(Viagem).filter((Viagem.data.between('1986-05-29','2023-05-19')) & (Viagem.adultos==adultos) & (Viagem.criancas==criancas)).all()",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(lista_itens)",
			""
		],
		"description": "Cria um select usando and"
	},
	"sqlalchemy select or": {
		"scope": "python",
		"prefix": "selectOr",
		"body": [
			"def getOr(adultos,criancas):",
			"",
			"\t#Viagem é o nome da tabela mapeada no orm('Classe'), o data,adultos e criancas são campos da tabela('atributos da classe')",
			"",
			"\tresult = session.query(Viagem).filter((Viagem.data.between('1986-05-29','2023-05-19')) | (Viagem.adultos==adultos) | (Viagem.criancas==criancas)).all()",
			"",
			"\tlista_itens = [item.dict() for item in result]",
			"",
			"\tsession.close()",
			"",
			"\treturn(lista_itens)",
			""
		],
		"description": "Cria um select usando and"
	},
	"sqlalchemy select count": {
		"scope": "python",
		"prefix": "selectCount",
		"body": [
			"def getCount():",
			"\tfrom sqlalchemy.sql import func",
			"",
			"\tresult = session.query(func.count(Cliente.id)).scalar()",
			"",
			"\tsession.close()",
			"",
			"\treturn(result)",
			""
		],
		"description": "Cria um select usando a função de agregação count"
	},

	"sqlalchemy select max": {
		"scope": "python",
		"prefix": "selectMax",
		"body": [
			"def getMax():",
			"\tfrom sqlalchemy.sql import func",
			"",
			"\tmax_valor = session.query(func.max(Exemplo.valor)).scalar()",
			"",
			"\tsession.close()",
			"",
			"\treturn(max_valor)",
			""
		],
		"description": "Cria um select usando a função de agregação max"
	},
	"sqlalchemy select avg": {
		"scope": "python",
		"prefix": "selectAVG",
		"body": [
			"def getAVG():",
			"\tfrom sqlalchemy.sql import func",
			"",
			"\tavg_amount = session.query(func.avg(Order.amount)).scalar()",
			"",
			"\tsession.close()",
			"",
			"\treturn(avg_amount)",
			""
		],
		"description": "Cria um select usando a função de agregação média"
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
	"sqlalchemy insert MxM": {
		"scope": "python",
		"prefix": "SQLAlchemyInsertMxM",
		"body": [
			"def insert_compra(compra_data: dict):",
			"\ttry:",
			"\t\tresultado = session.query(Cliente).filter(Cliente.id == compra_data['id']).first()",
			"\t\tcampos = compra_data['campo']",

			"\t\tcompra = Compra(",
			"\t\t\tid_Cliente = resultado.id",
			"\t\t)",
			
            "\t\tfor livro in livros:",
            "\t\t# Nessa parte vc tem que criar o objeto da table de livros e passar os atributos",
            
                "\t\t\tlivro_obj = Livro(",
                    "\t\t\t\tnome = livro['livro'],",
                    "\t\t\t\tautor = livro['autor'],",
                    "\t\t\t\teditora = livro['editora'],",
                "\t\t\t)",
                "\t\t\t# aqui vc adiciona os livros na tabela de junção entre livros e compras",
                "\t\t\tcompra.livro_objeto.append(livro_obj)",
			
			
			"\t\tsession.commit()",


			"\t\tdados_cadastrados={",
				"\t\t\t\t\"id_compra\": compra.id,",
				"\t\t\t\t\"id_cliente\": compra.id_cliente,",
				"\t\t\t\t\"livros\" : [{",
					"\t\t\t\t\t\"nome\":livro.nome,",
					"\t\t\t\t\t\"autor\":livro.autor,",
					"\t\t\t\t\t\"editora\":livro.editora",
				"\t\t\t\t}for livro in compra.livro_objeto]",
			"\t\t}",

			"\t\treturn dados_cadastrados",

			"\t\tsession.close()",
			
			"",
			"\texcept Exception as e:",
	
			"\t\tprint(e)",
	
			"\t\tsession.rollback()",

		],
		"description": "Cria um exemplo de inserção na tabela com relacionamento de muitos para muitos"
	},
	"sqlalchemy update MxM": {
		"scope": "python",
		"prefix": "SQLAlchemyUpdateMxM",
		"body": [
			"def update_compra(id: int,compra_data: dict):",
			"\ttry:",
			"\t\tcompra = session.query(Compra).filter(Compra.id == id).first()",
			"\t\tif compra:",

			"\t\t\tcliente = session.query(Cliente).filter(Cliente.nome == compra_data['nome']).first()",
			
			"\t\t\tif cliente:",
			"\t\t\t\tlivros_json = compra_data['livros']",
			"\t\t\t\tcodigos_livro=[]",
			"\t\t\t\t#Limpar os livros antigos é necessário",
			"\t\t\t\tcompra.livro_objeto.clear()",

			"\t\t\t\tfor livro in livros_json:",
			"\t\t\t\t\t#buscando o livro no banco",
			"\t\t\t\t\tcodigo = session.query(Livro).filter(Livro.nome == livro['nome']).first()",
			"\t\t\t\t\t#armazenando o codigo do livro buscando em uma lista",
			"\t\t\t\t\tcodigos_livro.append(codigo.id)",
			
			"\t\t\t\tfor compra_livro in codigos_livro:",
			"\t\t\t\t\t#Buscando um livro pelo id",
			"\t\t\t\t\tlivro = session.query(Livro).filter(Livro.id==compra_livro).first()",
			"\t\t\t\t\tif livro:",
			"\t\t\t\t\t\t#Inserindo na tabela de relacionamento",
			"\t\t\t\t\t\tcompra.livro_objeto.append(livro)",

			"\t\t\t\tsession.commit()",
			
            "\t\t\t\tdados_cadastrados={",
            "\t\t\t\t\t\"id_compra\": id,",
			"\t\t\t\t\t\"id_cliente\": compra.id_cliente,",
            "\t\t\t\t\t\"nome\": cliente.nome,",
            "\t\t\t\t\t\"livros\" : [{",
            "\t\t\t\t\t\t\"nome\":livro.nome,",
            "\t\t\t\t\t\t\"autor\":livro.autor,",
            "\t\t\t\t\t\t\"editora\":livro.editora",
            "\t\t\t\t\t}for livro in compra.livro_objeto]",
            "\t\t\t\t}",
			"\t\t\t\tsession.close()",
			"\t\t\t\tdados_cadastrados",

			"\t\telse:",
			"\t\t\t#Não achou compra",
			"\t\t\treturn None",
			"\texcept Exception as e:",
			"\t\tprint(e)",
			"\t\tsession.rollback()",
		],
		"description": "Cria um exemplo de atualização na tabela com relacionamento de muitos para muitos"
	},
	"sqlalchemy select_all MxM": {
		"scope": "python",
		"prefix": "SQLAlchemySelectAllMxM",
		"body": [
			"def buscar_compra_all():",
			"\ttry:",
			"\t\tresultados=[]",
			"\t\tcompras = session.query(Compra).all()",
			"\t\tif compras:",

			"\t\t\tfor compra in compras:",
			"\t\t\t\tlivros = []",
			"\t\t\t\tfor livro in compra.livro_objeto:",
			"\t\t\t\t\tlivro_data = LivroEntity(",
			"\t\t\t\t\t\tnome = livro.nome,",
			"\t\t\t\t\t\tautor = livro.autor,",
			"\t\t\t\t\t\teditora=livro.editora",
			"\t\t\t\t\t)",
			"\t\t\t\t\tlivros.append(livro_data)",

			"\t\t\t\tcliente = session.query(Cliente).filter(Cliente.id==compra.id_cliente).first()",
			"\t\t\t\tdados_compra = CompraEntity(",
			"\t\t\t\t\tid = compra.id,",
			"\t\t\t\t\tid_cliente = compra.id_cliente,",
			"\t\t\t\t\tnome= cliente.nome,",
			"\t\t\t\t\tlivros=livros",
			"\t\t\t\t)",
			"\t\t\t\tresultados.append(dados_compra)",
			"\t\t\tresultados = ListaCompraFinal(compras = resultados)",
			"\t\t\treturn resultados",
			"\t\telse:",
			"\t\t\treturn None",
			"\texcept Exception as e:",
			"\t\tprint(e)",
			"\t\tsession.rollback()",
		],
		"description": "Cria um exemplo de busca na tabela com relacionamento de muitos para muitos"
	},
	"sqlalchemy buscar_id MxM": {
		"scope": "python",
		"prefix": "SQLAlchemySelectIdMxM",
		"body": [
			"def select_compra_id(id: int,compra_data: dict):",
			"\ttry:",
			"\t\tcompra = session.query(Compra).filter(Compra.id == id).first()",
			"\t\tif compra:",
			"\t\t\tcliente = session.query(Cliente).filter(Cliente.id == compra.id_cliente).first()",
			"\t\t\tlivros = []",
			"\t\t\tfor livro in compra.livro_objeto:",
			"\t\t\t\tlivro_data = LivroEntity(",
			"\t\t\t\t\tnome = livro.nome,",
			"\t\t\t\t\tautor = livro.autor,",
			"\t\t\t\t\teditora=livro.editora",
			"\t\t\t\t)",
			"\t\t\t\tlivros.append(livro_data)",

			"",
			"\t\t\tdados_compra = CompraEntity(",
			"\t\t\t\tid = compra.id,",
			"\t\t\t\tid_cliente = compra.id_cliente,",
			"\t\t\t\tnome= cliente.nome,",
			"\t\t\t\tlivros=livros",
			"\t\t\t)",
			"\t\t\treturn dados_compra",
			"\t\telse:",
			"\t\t\treturn None",
			"\texcept Exception as e:",
			"\t\tprint(e)",
			"\t\tsession.rollback()",
		],
		"description": "Cria um exemplo de buscar por id na tabela com relacionamento de muitos para muitos"
	},
}