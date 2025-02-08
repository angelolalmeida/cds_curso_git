# Áreas de trabalho no GIT

## Working Directory

## Staging Area

## .git directory (Repository)

## Comandos Básicos

## Como iniciar um repositorio local

```md
```shell
#!/bin/bash
git init
```

## Verificar situação do repositório

```md
```shell
#!/bin/bash
git status
```

## Como adicionar um arquivo na área de staging

```md
```shell
#!/bin/bash
git add .
```

## Commitar um arquivo na Staging Area

```md
```shell
#!/bin/bash
git add .
git commit -m "Mensagem do commit"
```

## Desfazer as alterações no working directory

```md
```shell
  git restore <nome_do_arquivo>
```

## Remover arquivos da staging area

```md
```shell
  git restore -- staged <nome_do_arquivo>
```

## Visualizar histórico de commits

Mostra o hostórico de commits em apenas uma linha

```md
```shell
  git log --oneline
```

## Arrumar o histórico de commits

### Alterando o último commit

Para alterar a mensagem do ultimo commit

```md
```shell
  git commit -m "Mensagem" -- amend
```