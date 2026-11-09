# Codebase Conventions

Between each fork and downstream of Space Station 14, you'll often notice that each codebase has specific ways of doing things. This is a (hopefully) comprehensive guide on how *Funky Station* organizes its codebase, and a more general guide of what we do and don't want when creating and porting content.

Some of this information is repeated between [Macrocosm](https://docs.macrocosm.cool/docs/Conventions/pull-requests)'s and [WizDen](https://docs.spacestation14.com/en/general-development/codebase-info/conventions.html)'s conventions, and a lot of information between each holds true. I've tried to get the most important information down here, but there's no harm in reading the other two articles. Especially WizDen's, since the information there is true of the entire codebase rather than Funky-specific conventions.

## Content brought to Funky Station should match our license

Funky Station is licensed under the [MIT License](https://github.com/funky-station/forky-station/blob/master/LICENSES/MIT.txt). Any code ported or made for Funky Station must also be MIT. Exceptions to other compliant licenses may only be granted after talking to the maintainers and hosts, though this is generally not reliable.

AGPL is **not** a compliant license and any PRs with AGPL code, unless relicensed to MIT, will be automatically closed.

## Content must be properly namespaced

A "namespace" is a subfolder in the game's directories that represents content not made by WizDen. `_MACRO` only contains Macrocosm content added during an upstream merge, the same way WizDen content is added. As a Funky Station contributor, you shouldn't have to worry about putting anything in there.

All content PRed to Funky Station *must* be in a downstream's namespace. If it is wholely original work, then it must be under `_Funkystation`. If you are porting something, then the content should remain in its respective downstream namespace. For example, if I am porting something from Ephemeral Space, then the code should remain in the `_ES` namespace. If a codebase you are porting from does not namespace their own content, then please create a namespace for them. 

```admonish warning
Content being ported does not mean that these conventions do not apply. Please make sure any ported content still follows all of these, which may mean that you need to edit or refactor ported systems. 
```

### Use `partial` classes to namespace clean C# edits

If you are adding a new method to an already existing upstream class (either from WizDen or Macrocosm), you may be asked to move it to a partial class under our namespace. This means you would create a new file in our file structure, and then change the namespace declaration to match the original system. This allows you to cleanly extend the class and its using directives without having to copy paste everything over.

For example, if I want to add a new method called `AddTabbyStripes()` to the upstream `CatSystem`, I would not create the method in `Content.Server/Cats/CatSystem.cs`. Instead, I would create `Content.Server/_Funkystation/Cats/CatSystem.cs` and create my method there. Both classes would become partial, and I would call `AddTabbyStripes()` in the original system where necessary.

## Use the `Fu` prefix to replace entities or locale

There are times when entities change so drastically from their upstream version that it is easier to create new entities entirely. When we do this, we add the `Fu` prefix to the new entity id and create it in our namespace. You would then replace all of the usages of the old entity with the new id.

To "remove" the old entity, you can then make it abstract by adding `abstract: true` to the entity, or bulk abstract the entire file by adding it to `ignoredPrototypes.yml`. 

You can also add a line in `migration.yml` to migrate the old entity to the new one, for example adding the line `ClothingOuterWinterHos: FuClothingOuterWinterHos`. Migrations can be a little finicky, and are supposed to be a "temporary" solution, though, so use them sparingly. 

## Place resprites under `_Funkystation` namespace

Instead of replacing old sprites with new ones and editing the `meta.json` of an RSI, make an entirely new RSI in the `_Funkystation` namespace and replace the resource path of the entity. Assuming that the new resource path is the exact same as the original, with the added `_Funkystation` subfolder, this change does not need to be commented.

## Sprites should adhere to the Funky Station palette

We use a modified version of the SPLENDOR AAP palette, which you can find [here](https://github.com/vectorassembly/splendorstation/tree/main). Try to make sure you're using the newest version, since there will be more colors available. We also have a [beginner's guide](https://ellipsus.com/read/1JlZabybZn7IYUS26Y5agz/Funky-Art-Contribution-Beginners-Guide) to contributing art. 

## Content should be properly commented

You should have comments explaining *why* and *what* your code is doing, rather than assuming that code is self-documenting. Readable variable and class names are always good practice, but none of us are omnipresent and can immediately understand what you intended to do. Commenting your code helps lessen the burden on both your fellow contributors and maintainers. 

All methods, including event methods, that you make (and port!) should have a comment explaining what they are doing. Line-by-line comments should be used as needed, and are not inherently required. If your code requires a lot of line-by-comments to be understandable, you might want to consider breaking it up into multiple methods and summarizing those. 

## Comment changes made outside of `_Funkystation`

If you alter code, you must leave a comment to indicate that the code was altered and why it was altered. This is to prevent confusion during upstream merges and to ensure your edits do not get accidentally deleted. You may use inline edits to showcase how one line of code was changed, or `start` and `end` to indicate that an entire block was changed.

Building off of the prior section, it is especially important that you document *why* you edited something. If a maintainer does not understand why something was edited originally, and a refactor is pulled downwards, then it is likely that they will revert the change entirely. We need to understand why changes were done originally to be able to recreate them when systems are entirely refactored. 
