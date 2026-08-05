# Codebase Conventions

Between each fork and downstream of Space Station 14, you'll often notice that each codebase has specific ways of doing things. This is a (hopefully) comprehensive guide on how *Funky Station* organizes its codebase, and a more general guide of what we do and don't want when creating and porting content.

Some of this information is repeated between [Macrocosm](https://docs.macrocosm.cool/docs/Conventions/pull-requests)'s and [WizDen](https://docs.spacestation14.com/en/general-development/codebase-info/conventions.html)'s conventions, and a lot of information between each holds true. I've tried to get the most important information down here, but there's no harm in reading the other two articles. Especially WizDen's, since the information there is true of the entire codebase rather than Funky-specific conventions.

## Content brought to Funky Station should match our license

Funky Station is licensed under the [MIT License](https://github.com/funky-station/forky-station/blob/master/LICENSES/MIT.txt). Any code ported or made for Funky Station must also be MIT. Exceptions to other compliant licenses may only be granted after talking to the maintainers and hosts, though this is generally not reliable.

AGPL is **not** a compliant license and any PRs with AGPL code, unless relicensed to MIT, will be automatically closed.

## Content must be properly namespaced

A "namespace" is a subfolder in the game's directories that represents content not made by WizDen. There are two subfolders within Funky Station's codebase: `_MACRO` and `_Funkystation` (\*Soon). `_MACRO` is only contain Macrocosm content added during an upstream merge, the same way WizDen content is. As a Funky Station contributor, you shouldn't have to worry about putting anything in there.

All content PRed to Funky Station *must* be in the `_Funkystation` namespace. This *includes* any ports from other stations, rather than keeping them in their respective downstream's namespace.

### Why not keep other downstream content in their original namespace? (ex. `_Impstation` or `_DV`)

There are two main reasons for this. One, it keeps the codebase a little neater. Rather than having to memorize what content comes from where, it should be fairly easy to navigate each subfolder. Two, you should not be porting content from other servers without any edits or thought about how those features might fit into Funky Station specifically.

Each downstream of Space Station 14 plays differently, and content usually can't be unanimously ported from one fork to another. When porting content, you should think about ways the system might interact in our setting specifically, which might mean rewriting portions of the systems.

Originally, ported content was kept in its original namespace so bugfixes could be ported easier. However, bugfixes are rarely ported consistently, unless they are from a source we merge from consistently (so, a codebase we have a direct downstream relationship with). 

### Use `partial` classes to namespace clean C# edits

If you are adding a new method to an already existing upstream system (either from WizDen or Macrocosm), you may be asked to move it to a partial system under our namespace. This means you would create a new file in our file structure, and then change the namespace declaration to match the original system. This allows you to cleanly extended the system and its using directives without having to copy paste everything over.

For example, if I want to add a new method called `AddTabbyStripes()` to the upstream `CatSystem`, I would not create the method in `Content.Server/Cats/CatSystem.cs`. Instead, I would create `Content.Server/_Funkystation/Cats/CatSystem.cs` and create my method there. Both classes would become partial, and I would call `AddTabbyStripes()` in the original system where necessary.

## Use the `Fu` prefix to replace entities or locale

There are times when entities change so drastically from their upstream version that it is easier to create new entities entirely. When we do this, we add the `Fu` prefix to the new entity id and create it in our namespace. You would then replace all of the usages of the old entity with the new id.

To "remove" the old entity, you can then make it abstract by adding `abstract: true` to the entity, or bulk abstract the entire file by adding it to `ignoredPrototypes.yml`. You can also add a line in `migration.yml` to migrate the old entity to the new one, for example adding the line `ClothingOuterWinterHos: FuClothingOuterWinterHos`.

## Place resprites under `_Funkystation` namespace

Instead of replacing old sprites with new ones and editing the `meta.json` of an RSI, make an entirely new RSI in the `_Funkystation` namespace and replace the resource path of the entity. Assuming that the new resource path is the exact same as the original, with the added `_Funkystation` subfolder, this change does not need to be commented.

## Content should be properly commented

All code should have comments explaining *what* and *why* it is doing. Do not assume that code is self-documenting. Readable variable and class names is always good practice, but even with that, not all code is self-documenting. This also lessens the burden on your fellow contributors and maintainers; none of us are omnipresent and can immediately understand what you intended to do. Commenting your code, and even including some of your thought process, can help everyone better build and improve the codebase.

## Comment changes made outside of `_Funkystation`

If you alter code, you must leave a comment to indicate that the code was altered and why it was altered. This is to prevent confusion during upstream merges and to ensure your edits do not get accidentally deleted. You may use inline edits to showcase how one line of code was changed, or `start` and `end` to indicate that an entire block was changed.

Building off of the prior section, it is especially important that you document *why* you edited something. If a maintainer does not understand why something was edited originally, and a refactor is pulled downwards, then it is likely that they will revert the change entirely. We need to understand why changes were done originally to be able to recreate them when systems are entirely refactored. 
